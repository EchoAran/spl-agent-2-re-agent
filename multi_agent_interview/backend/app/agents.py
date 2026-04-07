from __future__ import annotations

import asyncio
import json
import shutil
import sys
import uuid
from pathlib import Path
from typing import Any, Protocol

from .llm import LLMServices
from .models import ChatMessage, InterviewRoundContext, LLMConfig
from .skills import FileSandbox, Skill, format_skills_for_prompt


class AgentRuntime(Protocol):
    id: str
    name: str
    role: str
    can_use_skills: bool

    async def respond(self, context: InterviewRoundContext, prompt: str | None = None) -> ChatMessage:
        ...


class SkillStateStore:
    def __init__(self, state_root: Path, session_id: str):
        self.state_root = state_root.resolve()
        self.session_id = session_id
        self.session_dir = self.state_root / "state" / "sessions" / self.session_id
        self._lock = asyncio.Lock()

    @staticmethod
    def _atomic_write(path: Path, payload: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = path.with_suffix(path.suffix + ".tmp")
        tmp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp_path.replace(path)

    @staticmethod
    def _safe_json_read(path: Path, default_value: Any) -> Any:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default_value

    @staticmethod
    def _safe_text_read(path: Path, default_value: str) -> str:
        try:
            return path.read_text(encoding="utf-8")
        except Exception:
            return default_value

    @property
    def session_state_dir(self) -> str:
        return self.session_dir.as_posix()

    def resolve_path(self, file_path: str) -> Path:
        raw = file_path.replace("\\", "/").strip()
        candidate = Path(raw)
        if candidate.is_absolute():
            resolved = candidate.resolve()
        else:
            resolved = (self.state_root / candidate).resolve()
        try:
            resolved.relative_to(self.state_root)
        except ValueError as exc:
            raise PermissionError(f"Path out of skill root: {file_path}") from exc
        return resolved

    async def ensure_dir(self, dir_path: str) -> str:
        async with self._lock:
            target = self.resolve_path(dir_path)
            target.mkdir(parents=True, exist_ok=True)
            return target.as_posix()

    async def read_text_file(self, file_path: str) -> dict[str, Any]:
        async with self._lock:
            target = self.resolve_path(file_path)
            if not target.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            return {"resolved_path": target.as_posix(), "content": self._safe_text_read(target, "")}

    async def write_text_file(self, file_path: str, content: str) -> dict[str, Any]:
        async with self._lock:
            target = self.resolve_path(file_path)
            target.parent.mkdir(parents=True, exist_ok=True)
            tmp_path = target.with_suffix(target.suffix + ".tmp")
            tmp_path.write_text(content, encoding="utf-8")
            tmp_path.replace(target)
            return {"resolved_path": target.as_posix()}

    async def read_json_file(self, file_path: str) -> dict[str, Any]:
        async with self._lock:
            target = self.resolve_path(file_path)
            if not target.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            data = self._safe_json_read(target, None)
            if data is None:
                raise ValueError(f"Invalid JSON file: {file_path}")
            return {"resolved_path": target.as_posix(), "content": data}

    async def write_json_file(self, file_path: str, content: Any) -> dict[str, Any]:
        async with self._lock:
            target = self.resolve_path(file_path)
            self._atomic_write(target, content)
            return {"resolved_path": target.as_posix()}

    async def append_json_array(self, file_path: str, item: Any) -> dict[str, Any]:
        async with self._lock:
            target = self.resolve_path(file_path)
            array_data = self._safe_json_read(target, [])
            if not isinstance(array_data, list):
                array_data = []
            array_data.append(item)
            self._atomic_write(target, array_data)
            return {"resolved_path": target.as_posix(), "length": len(array_data)}

    async def cleanup(self) -> None:
        async with self._lock:
            if self.session_dir.exists():
                shutil.rmtree(self.session_dir, ignore_errors=True)


class InterviewerSkillAgent:
    def __init__(
        self,
        llm: LLMServices,
        skills: list[Skill],
        sandbox: FileSandbox,
        state_root: Path,
        session_id: str,
    ):
        self.id = "interviewer"
        self.name = "系统访谈者"
        self.role = "interviewer"
        self.can_use_skills = True
        self.llm = llm
        self.skills = skills
        self.sandbox = sandbox
        self.state_store = SkillStateStore(state_root=state_root, session_id=session_id)
        self.session_id = session_id
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "description": "Read UTF-8 text from skill files using forward-slash paths.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Absolute or relative file path.",
                            }
                        },
                        "required": ["file_path"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_skill_runtime_context",
                    "description": "Return skill root, session_id and recommended session state directory.",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "cleanup_skill_state",
                    "description": "Delete current session state directory under skill-defined state path.",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "read_skill_text",
                    "description": "Read UTF-8 text file under skill root for custom state machine files.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"},
                        },
                        "required": ["file_path"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "write_skill_text",
                    "description": "Write UTF-8 text file under skill root for custom state machine files.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"},
                            "content": {"type": "string"},
                        },
                        "required": ["file_path", "content"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "ensure_skill_dir",
                    "description": "Create directory for skill state files under skill root.",
                    "parameters": {
                        "type": "object",
                        "properties": {"dir_path": {"type": "string"}},
                        "required": ["dir_path"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "read_skill_json",
                    "description": "Read JSON file under skill root for state machine.",
                    "parameters": {
                        "type": "object",
                        "properties": {"file_path": {"type": "string"}},
                        "required": ["file_path"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "write_skill_json",
                    "description": "Write JSON file under skill root for state machine.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"},
                            "content": {},
                        },
                        "required": ["file_path", "content"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "append_skill_json_array",
                    "description": "Append one item into a JSON array file under skill root.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"},
                            "item": {},
                        },
                        "required": ["file_path", "item"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
        ]

    def _build_system_prompt(self) -> str:
        return (
            "你是一个会使用 skills 的会话代理。"
            "当前任务是需求访谈，必须优先使用 requirements-elicitation skill。"
            "行为约束、访谈流程、结束条件都以 skill 内容为准，不要自创规则。"
            "读取文件时只允许读取 SKILL.md 或 SKILL.md 明确引用的路径，不要猜测诸如 config.json 这类未声明文件。"
            "如果 skill 涉及状态管理，请先调用 get_skill_runtime_context 获取可用根路径与session目录建议，再按skill文档自行拼接路径。"
            "状态文件的创建、读取、写入、数组追加请使用 ensure_skill_dir/read_skill_text/write_skill_text/read_skill_json/write_skill_json/append_skill_json_array。"
            f"当前会话ID是 {self.session_id}，默认状态根目录是 {self.state_store.state_root.as_posix()}。"
            "当完成条件满足时，输出最终结果并在末尾附加 [[INTERVIEW_COMPLETE]]。"
            "访谈进行中时每轮只输出一段短句，不超过120字，默认只问一个关键问题。"
            "若用户要求暂停，你只需等待，不要主动推进。"
            "你可以用 read_file 工具读取技能目录内容。"
            "\n可用 skills:\n"
            + format_skills_for_prompt(self.skills)
        )

    async def _chat_with_tools(self, messages: list[dict[str, Any]]) -> str:
        for _ in range(8):
            result = await self.llm.chat(messages=messages, tools=self.tools, tool_choice="auto")
            message = result["message"]
            finish_reason = result["finish_reason"]

            assistant_message: dict[str, Any] = {
                "role": "assistant",
                "content": message.get("content", ""),
            }
            if message.get("tool_calls"):
                assistant_message["tool_calls"] = message["tool_calls"]
            messages.append(assistant_message)

            tool_calls = message.get("tool_calls") or []
            if finish_reason != "tool_calls" or not tool_calls:
                return str(message.get("content", ""))

            for tool_call in tool_calls:
                function_block = tool_call.get("function", {}) if isinstance(tool_call, dict) else {}
                tool_name = str(function_block.get("name", "")).strip()
                raw_arguments = function_block.get("arguments", "{}")
                if not isinstance(raw_arguments, str):
                    raw_arguments = json.dumps(raw_arguments, ensure_ascii=False)
                try:
                    arguments = json.loads(raw_arguments)
                except json.JSONDecodeError as exc:
                    tool_output = f"TOOL_ERROR: invalid JSON arguments: {exc}"
                else:
                    if tool_name == "read_file":
                        file_path = str(arguments.get("file_path", "")).strip()
                        if not file_path:
                            tool_output = "TOOL_ERROR: missing file_path"
                        else:
                            try:
                                content_text, resolved_path = self.sandbox.read_text(file_path)
                                tool_output = json.dumps(
                                    {
                                        "ok": True,
                                        "resolved_path": resolved_path,
                                        "content": content_text,
                                    },
                                    ensure_ascii=False,
                                )
                            except Exception as exc:
                                if isinstance(exc, FileNotFoundError):
                                    tool_output = (
                                        "TOOL_ERROR: FileNotFoundError: target file not found. "
                                        "Do not guess filenames. Read SKILL.md first and only access explicitly referenced files."
                                    )
                                else:
                                    tool_output = f"TOOL_ERROR: {type(exc).__name__}: {exc}"
                    elif tool_name == "get_skill_runtime_context":
                        tool_output = json.dumps(
                            {
                                "ok": True,
                                "skill_root": self.state_store.state_root.as_posix(),
                                "session_id": self.session_id,
                                "recommended_session_state_dir": self.state_store.session_state_dir,
                            },
                            ensure_ascii=False,
                        )
                    elif tool_name == "cleanup_skill_state":
                        await self.state_store.cleanup()
                        tool_output = json.dumps({"ok": True}, ensure_ascii=False)
                    elif tool_name == "ensure_skill_dir":
                        dir_path = str(arguments.get("dir_path", "")).strip()
                        if not dir_path:
                            tool_output = "TOOL_ERROR: missing dir_path"
                        else:
                            resolved_path = await self.state_store.ensure_dir(dir_path)
                            tool_output = json.dumps({"ok": True, "resolved_path": resolved_path}, ensure_ascii=False)
                    elif tool_name == "read_skill_text":
                        file_path = str(arguments.get("file_path", "")).strip()
                        if not file_path:
                            tool_output = "TOOL_ERROR: missing file_path"
                        else:
                            try:
                                result = await self.state_store.read_text_file(file_path)
                                tool_output = json.dumps({"ok": True, **result}, ensure_ascii=False)
                            except Exception as exc:
                                tool_output = f"TOOL_ERROR: {type(exc).__name__}: {exc}"
                    elif tool_name == "read_skill_json":
                        file_path = str(arguments.get("file_path", "")).strip()
                        if not file_path:
                            tool_output = "TOOL_ERROR: missing file_path"
                        else:
                            try:
                                result = await self.state_store.read_json_file(file_path)
                                tool_output = json.dumps({"ok": True, **result}, ensure_ascii=False)
                            except Exception as exc:
                                tool_output = f"TOOL_ERROR: {type(exc).__name__}: {exc}"
                    elif tool_name == "write_skill_json":
                        file_path = str(arguments.get("file_path", "")).strip()
                        if not file_path:
                            tool_output = "TOOL_ERROR: missing file_path"
                        else:
                            try:
                                result = await self.state_store.write_json_file(file_path, arguments.get("content"))
                                tool_output = json.dumps({"ok": True, **result}, ensure_ascii=False)
                            except Exception as exc:
                                tool_output = f"TOOL_ERROR: {type(exc).__name__}: {exc}"
                    elif tool_name == "write_skill_text":
                        file_path = str(arguments.get("file_path", "")).strip()
                        if not file_path:
                            tool_output = "TOOL_ERROR: missing file_path"
                        else:
                            try:
                                result = await self.state_store.write_text_file(
                                    file_path, str(arguments.get("content", ""))
                                )
                                tool_output = json.dumps({"ok": True, **result}, ensure_ascii=False)
                            except Exception as exc:
                                tool_output = f"TOOL_ERROR: {type(exc).__name__}: {exc}"
                    elif tool_name == "append_skill_json_array":
                        file_path = str(arguments.get("file_path", "")).strip()
                        if not file_path:
                            tool_output = "TOOL_ERROR: missing file_path"
                        else:
                            try:
                                result = await self.state_store.append_json_array(file_path, arguments.get("item"))
                                tool_output = json.dumps({"ok": True, **result}, ensure_ascii=False)
                            except Exception as exc:
                                tool_output = f"TOOL_ERROR: {type(exc).__name__}: {exc}"
                    else:
                        tool_output = f"TOOL_ERROR: unsupported tool: {tool_name}"
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.get("id", ""),
                        "content": tool_output,
                    }
                )
        return "我需要更多上下文来继续访谈，请补充你当前最关注的业务目标。"

    async def respond(self, context: InterviewRoundContext, prompt: str | None = None) -> ChatMessage:
        transcript = "\n".join(
            [f"{item.agent_name}({item.role}): {item.text}" for item in context.transcript[-30:]]
        )
        runtime_prompt = prompt or "请基于当前上下文继续。"
        messages = [
            {"role": "system", "content": self._build_system_prompt()},
            {
                "role": "user",
                "content": (
                    f"当前第 {context.round_index} 轮。用户输入：{context.user_input}\n"
                    f"会话状态：{context.metadata.get('session_status', 'running')}\n"
                    f"会话ID：{context.metadata.get('session_id', 'unknown')}\n"
                    f"上下文对话：\n{transcript}\n"
                    f"当前任务：{runtime_prompt}\n"
                    "输出要求：访谈阶段仅输出简短一句；若结束则按skill要求输出总结并带 [[INTERVIEW_COMPLETE]]。"
                ),
            },
        ]
        content = await self._chat_with_tools(messages)
        return ChatMessage(
            id=str(uuid.uuid4()),
            agent_id=self.id,
            agent_name=self.name,
            role=self.role,
            text=content.strip(),
            round_index=context.round_index,
        )


class SPLRespondentAgent:
    def __init__(
        self,
        agent_id: str,
        name: str,
        llm_config: LLMConfig,
        workspace_root: Path,
        github_repo_url: str,
        project_name: str | None = None,
    ):
        self.id = agent_id
        self.name = name
        self.role = "respondent"
        self.can_use_skills = False
        self.llm_config = llm_config
        self.workspace_root = workspace_root.resolve()
        self.github_repo_url = github_repo_url
        self.project_name = project_name
        self._service: Any = None
        self._project_id: str | None = None
        self._project_name: str | None = None
        self._project_lock = asyncio.Lock()

    def _service_instance(self) -> Any:
        if self._service is not None:
            return self._service
        candidates = [
            self.workspace_root / "spl_agent",
            self.workspace_root.parent / "spl_agent",
            Path.cwd() / "spl_agent",
        ]
        spl_root = next((item.resolve() for item in candidates if item.exists()), candidates[1].resolve())
        spl_root_str = str(spl_root)
        if spl_root_str not in sys.path:
            sys.path.insert(0, spl_root_str)
        from spl_system.core.config import LLMConfig as SPLLLMConfig
        from spl_system.core.service import SPLProjectService

        cache_dir = self.workspace_root.parent / ".spl_i"
        llm_cfg = SPLLLMConfig(
            api_key=self.llm_config.api_key,
            base_url=self.llm_config.base_url,
            model=self.llm_config.model,
            temperature=0.0,
            timeout_sec=180,
        )
        self._service = SPLProjectService(
            base_dir=spl_root,
            llm_config=llm_cfg,
            cache_dir=cache_dir,
            max_rounds=12,
            build_workers=4,
        )
        return self._service

    async def _ensure_project_ready(self) -> None:
        if self._project_id:
            return
        async with self._project_lock:
            if self._project_id:
                return
            result = await asyncio.to_thread(
                self._service_instance().build_project,
                target=self.github_repo_url,
                project_name=self.project_name,
                source_type="git",
                prefer_legacy_spl=False,
                force_rebuild=False,
                use_llm_for_build=True,
                export_spl=True,
            )
            self._project_id = str(result["project_id"])
            self._project_name = str(result.get("project_name") or "")

    async def _ask_repository(self, question: str) -> str:
        await self._ensure_project_ready()
        project_id = self._project_id or ""
        result = await asyncio.to_thread(self._service_instance().ask, project_id, question)
        return str(result.answer).strip()

    async def respond(self, context: InterviewRoundContext, prompt: str | None = None) -> ChatMessage:
        transcript = "\n".join([f"{item.agent_name}({item.role}): {item.text}" for item in context.transcript[-20:]])
        interviewer_prompt = prompt or "请补充需求事实。"
        question = (
            f"你是代码仓库访谈中的技术受访者。\n"
            f"仓库地址：{self.github_repo_url}\n"
            f"当前轮次：{context.round_index}\n"
            f"用户补充：{context.user_input}\n"
            f"系统代理提问：{interviewer_prompt}\n"
            f"最近对话：\n{transcript}\n"
            "请基于仓库实际结构给出直接回答，优先输出可验证的模块、函数、流程和约束。"
        )
        try:
            text = await self._ask_repository(question)
        except Exception as exc:
            text = f"spl_agent 查询失败：{type(exc).__name__}: {exc}"
        return ChatMessage(
            id=str(uuid.uuid4()),
            agent_id=self.id,
            agent_name=self.name,
            role=self.role,
            text=text,
            round_index=context.round_index,
        )
