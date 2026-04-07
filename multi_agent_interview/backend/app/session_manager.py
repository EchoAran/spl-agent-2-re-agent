from __future__ import annotations

import asyncio
import contextlib
import json
import logging
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import aiohttp
from fastapi import WebSocket

from .agents import InterviewerSkillAgent, SPLRespondentAgent
from .llm import LLMServices, load_llm_config
from .models import ChatMessageResponse, CreateSessionRequest, SessionMessagesResponse
from .orchestrator import InterviewOrchestrator
from .skills import FileSandbox, scan_skills

logger = logging.getLogger("multi_agent_interview.session")


@dataclass
class InterviewSession:
    id: str
    enabled_agent_ids: list[str]
    interviewer_agent_id: str
    aiohttp_session: aiohttp.ClientSession
    orchestrator: InterviewOrchestrator
    status: str = "running"
    complete_reason: str | None = None
    websockets: set[WebSocket] = field(default_factory=set)
    input_queue: asyncio.Queue[str] = field(default_factory=asyncio.Queue)
    runner_task: asyncio.Task[None] | None = None
    last_user_input: str = ""
    messages: list[ChatMessageResponse] = field(default_factory=list)
    cache_file_path: Path | None = None


class SessionManager:
    def __init__(self, skill_roots: list[Path], workspace_root: Path):
        self.skill_roots = [item.resolve() for item in skill_roots]
        self.workspace_root = workspace_root.resolve()
        self.cache_dir = self.workspace_root / "backend" / "runtime" / "session_cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.sessions: dict[str, InterviewSession] = {}
        self._runner_lock = asyncio.Lock()

    async def create_session(self, request: CreateSessionRequest) -> InterviewSession:
        github_repo_url = request.github_repo_url.strip()
        if not github_repo_url:
            raise ValueError("github_repo_url is required")
        project_name = (request.project_name or "").strip() or None
        session_id = str(uuid.uuid4())
        timeout = aiohttp.ClientTimeout(total=300)
        aiohttp_session = aiohttp.ClientSession(timeout=timeout)
        config = load_llm_config(self.workspace_root / "backend" / ".env")
        llm = LLMServices(session=aiohttp_session, config=config)

        all_skills = scan_skills(self.skill_roots)
        skills = [item for item in all_skills if item.name == "requirements-elicitation"]
        if not skills:
            await aiohttp_session.close()
            raise ValueError("missing required skill: requirements-elicitation")
        sandbox = FileSandbox(allowed_roots=self.skill_roots + [self.workspace_root], skills=skills)
        interviewer = InterviewerSkillAgent(
            llm=llm,
            skills=skills,
            sandbox=sandbox,
            state_root=Path(skills[0].location),
            session_id=session_id,
        )

        respondents = [
            SPLRespondentAgent(
                agent_id="spl_repo_respondent",
                name="SPL仓库受访者",
                llm_config=config,
                workspace_root=self.workspace_root,
                github_repo_url=github_repo_url,
                project_name=project_name,
            )
        ]

        session = InterviewSession(
            id=session_id,
            enabled_agent_ids=[item.id for item in respondents],
            interviewer_agent_id=interviewer.id,
            aiohttp_session=aiohttp_session,
            orchestrator=InterviewOrchestrator(interviewer=interviewer, respondents=respondents),
            status="running",
            cache_file_path=self.cache_dir / f"{session_id}.json",
        )
        self.sessions[session_id] = session
        self._flush_cache(session)
        logger.info("create_session id=%s enabled_agents=%s", session_id, session.enabled_agent_ids)
        return session

    def get(self, session_id: str) -> InterviewSession | None:
        return self.sessions.get(session_id)

    def get_messages(self, session_id: str) -> SessionMessagesResponse:
        session = self.get(session_id)
        if session:
            return SessionMessagesResponse(
                session_id=session.id,
                interviewer_agent_id=session.interviewer_agent_id,
                status=session.status,
                reason=session.complete_reason,
                messages=session.messages,
            )
        cache_file = self.cache_dir / f"{session_id}.json"
        if not cache_file.exists():
            raise ValueError("Session not found")
        try:
            data = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception as exc:
            raise ValueError(f"Session cache broken: {exc}") from exc
        messages = [ChatMessageResponse.model_validate(item) for item in data.get("messages", [])]
        return SessionMessagesResponse(
            session_id=str(data.get("session_id", session_id)),
            interviewer_agent_id=str(data.get("interviewer_agent_id", "interviewer")),
            status=str(data.get("status", "unknown")),
            reason=data.get("reason"),
            messages=messages,
        )

    async def attach_ws(self, session_id: str, websocket: WebSocket) -> None:
        session = self.get(session_id)
        if not session:
            return
        session.websockets.add(websocket)

    async def detach_ws(self, session_id: str, websocket: WebSocket) -> None:
        session = self.get(session_id)
        if not session:
            return
        session.websockets.discard(websocket)

    async def push_user_input(self, session_id: str, text: str) -> None:
        session = self.get(session_id)
        if not session:
            return
        await session.input_queue.put(text)

    async def pause(self, session_id: str, reason: str | None = None) -> None:
        session = self.get(session_id)
        if not session or session.status == "completed":
            return
        session.status = "paused"
        session.complete_reason = reason or "用户手动暂停"
        self._flush_cache(session)
        logger.info("pause_session id=%s reason=%s", session_id, session.complete_reason)

    async def resume(self, session_id: str) -> None:
        session = self.get(session_id)
        if not session or session.status == "completed":
            return
        session.status = "running"
        session.complete_reason = None
        self._flush_cache(session)
        logger.info("resume_session id=%s", session_id)

    async def start_runner_if_needed(self, session_id: str) -> None:
        session = self.get(session_id)
        if not session:
            return
        async with self._runner_lock:
            task = session.runner_task
            if task and not task.done():
                return
            session.runner_task = asyncio.create_task(self._run_session_loop(session))

    async def _broadcast(self, session: InterviewSession, payload: dict[str, Any]) -> None:
        disconnected: list[WebSocket] = []
        for socket in list(session.websockets):
            try:
                await socket.send_json(payload)
            except Exception:
                disconnected.append(socket)
        for socket in disconnected:
            session.websockets.discard(socket)

    def _flush_cache(self, session: InterviewSession) -> None:
        if not session.cache_file_path:
            return
        session.cache_file_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "session_id": session.id,
            "interviewer_agent_id": session.interviewer_agent_id,
            "status": session.status,
            "reason": session.complete_reason,
            "messages": [item.model_dump() for item in session.messages],
        }
        session.cache_file_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    async def _run_session_loop(self, session: InterviewSession) -> None:
        if session.status == "completed":
            return
        logger.info("runner_started session_id=%s", session.id)
        await self._broadcast(
            session,
            {"type": "session_status", "status": session.status, "reason": session.complete_reason},
        )
        while True:
            if session.status == "completed":
                self._flush_cache(session)
                await self._broadcast(
                    session,
                    {"type": "session_status", "status": "completed", "reason": session.complete_reason},
                )
                return
            if session.status == "paused":
                await asyncio.sleep(0.15)
                continue

            has_input = False
            newest_input = session.last_user_input
            try:
                newest_input = session.input_queue.get_nowait()
                has_input = True
                while True:
                    newest_input = session.input_queue.get_nowait()
            except asyncio.QueueEmpty:
                pass
            if not has_input:
                await asyncio.sleep(0.15)
                continue
            session.last_user_input = newest_input

            try:
                async for item, is_complete, reason in session.orchestrator.run_round_stream(
                    user_input=newest_input,
                    enabled_agent_ids=session.enabled_agent_ids,
                    session_status=session.status,
                    session_id=session.id,
                ):
                    message = ChatMessageResponse(
                        id=item.id,
                        agent_id=item.agent_id,
                        agent_name=item.agent_name,
                        role=item.role,
                        text=item.text,
                        round_index=item.round_index,
                    )
                    session.messages.append(message)
                    self._flush_cache(session)
                    await self._broadcast(
                        session,
                        {
                            "type": "message",
                            "message": message.model_dump(),
                        },
                    )
                    if is_complete:
                        session.status = "completed"
                        session.complete_reason = reason
                        self._flush_cache(session)
                        logger.info("session_completed id=%s reason=%s", session.id, reason)
                        break
            except Exception as exc:
                session.status = "paused"
                session.complete_reason = f"访谈执行异常，已自动暂停: {type(exc).__name__}: {exc}"
                self._flush_cache(session)
                logger.exception("runner_error session_id=%s", session.id)
                await self._broadcast(
                    session,
                    {"type": "session_status", "status": session.status, "reason": session.complete_reason},
                )
                await asyncio.sleep(0.3)
                continue
            await asyncio.sleep(0.2)

    async def close_session(self, session_id: str) -> None:
        session = self.sessions.pop(session_id, None)
        if not session:
            return
        if session.runner_task and not session.runner_task.done():
            session.runner_task.cancel()
            with contextlib.suppress(BaseException):
                await session.runner_task
        await session.aiohttp_session.close()
        logger.info("close_session id=%s", session_id)

    async def close_all(self) -> None:
        for session_id in list(self.sessions):
            await self.close_session(session_id)
