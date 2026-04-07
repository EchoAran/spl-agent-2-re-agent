from __future__ import annotations

import contextlib
import json
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.websockets import WebSocketState

from .models import (
    ClientEvent,
    CreateSessionRequest,
    SessionMessagesResponse,
    SessionResponse,
    SessionStatusResponse,
)
from .session_manager import SessionManager


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_DIR = PROJECT_ROOT / "frontend"
SKILLS_DIR = PROJECT_ROOT / "backend" / "skills"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("multi_agent_interview.app")

app = FastAPI(title="Multi Agent Interview Chatbox")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session_manager = SessionManager(
    skill_roots=[SKILLS_DIR],
    workspace_root=PROJECT_ROOT,
)

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")


@app.post("/api/sessions", response_model=SessionResponse)
async def create_session(request: CreateSessionRequest) -> SessionResponse:
    try:
        session = await session_manager.create_session(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    logger.info("session_created id=%s enabled_agents=%s", session.id, session.enabled_agent_ids)
    await session_manager.push_user_input(session.id, "请开始需求访谈。")
    await session_manager.start_runner_if_needed(session.id)
    return SessionResponse(
        session_id=session.id,
        enabled_agent_ids=session.enabled_agent_ids,
        interviewer_agent_id=session.interviewer_agent_id,
        status=session.status,
    )


@app.get("/api/sessions/{session_id}/status", response_model=SessionStatusResponse)
async def get_session_status(session_id: str) -> SessionStatusResponse:
    try:
        snapshot = session_manager.get_messages(session_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Session not found")
    return SessionStatusResponse(
        session_id=snapshot.session_id,
        status=snapshot.status,
        reason=snapshot.reason,
    )


@app.get("/api/sessions/{session_id}/messages", response_model=SessionMessagesResponse)
async def get_session_messages(session_id: str) -> SessionMessagesResponse:
    try:
        return session_manager.get_messages(session_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/api/sessions/{session_id}/pause", response_model=SessionStatusResponse)
async def pause_session(session_id: str) -> SessionStatusResponse:
    session = session_manager.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    await session_manager.pause(session_id, "用户手动暂停")
    logger.info("session_paused id=%s", session_id)
    return SessionStatusResponse(
        session_id=session.id,
        status=session.status,
        reason=session.complete_reason,
    )


@app.post("/api/sessions/{session_id}/resume", response_model=SessionStatusResponse)
async def resume_session(session_id: str) -> SessionStatusResponse:
    session = session_manager.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    await session_manager.resume(session_id)
    await session_manager.start_runner_if_needed(session_id)
    logger.info("session_resumed id=%s", session_id)
    return SessionStatusResponse(
        session_id=session.id,
        status=session.status,
        reason=session.complete_reason,
    )


@app.websocket("/ws/{session_id}")
async def ws_chat(websocket: WebSocket, session_id: str) -> None:
    session = session_manager.get(session_id)
    if not session:
        await websocket.close(code=4404, reason="Session not found")
        return

    await websocket.accept()
    logger.info("ws_connected session_id=%s", session_id)
    await session_manager.attach_ws(session_id, websocket)
    await session_manager.start_runner_if_needed(session_id)
    await websocket.send_json(
        {"type": "session_status", "status": session.status, "reason": session.complete_reason}
    )
    try:
        while True:
            raw_data = await websocket.receive_text()
            data = json.loads(raw_data)
            event = ClientEvent.model_validate(data)
            if event.type == "user_message" and event.text:
                logger.info("ws_user_message session_id=%s text_preview=%s", session_id, event.text[:200])
                await session_manager.push_user_input(session_id, event.text)
                continue
            if event.type == "pause":
                await session_manager.pause(session_id, "用户手动暂停")
                await websocket.send_json(
                    {"type": "session_status", "status": session.status, "reason": session.complete_reason}
                )
                continue
            if event.type == "resume":
                await session_manager.resume(session_id)
                await session_manager.start_runner_if_needed(session_id)
                await websocket.send_json(
                    {"type": "session_status", "status": session.status, "reason": session.complete_reason}
                )
                continue
            if event.type == "start":
                await session_manager.resume(session_id)
                await session_manager.start_runner_if_needed(session_id)
                await websocket.send_json(
                    {"type": "session_status", "status": session.status, "reason": session.complete_reason}
                )
                continue
            if event.type == "ping":
                await websocket.send_json({"type": "pong"})
                continue
            if event.type == "status":
                await websocket.send_json(
                    {"type": "session_status", "status": session.status, "reason": session.complete_reason}
                )
                continue
            if event.type != "user_message":
                await websocket.send_json({"type": "error", "text": "无效事件"})
                continue
    except WebSocketDisconnect:
        logger.info("ws_disconnected session_id=%s", session_id)
        return
    except Exception as exc:
        logger.exception("ws_error session_id=%s", session_id)
        with contextlib.suppress(RuntimeError):
            await websocket.send_json({"type": "error", "text": f"服务异常: {type(exc).__name__}: {exc}"})
    finally:
        await session_manager.detach_ws(session_id, websocket)
        if websocket.application_state != WebSocketState.DISCONNECTED:
            with contextlib.suppress(RuntimeError):
                await websocket.close()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await session_manager.close_all()
