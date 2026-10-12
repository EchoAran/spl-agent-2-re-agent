from __future__ import annotations

import asyncio
import json
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Protocol

from .llm import LLMServices
from .models import ChatMessage, InterviewRoundContext, LLMConfig
from .repository_qa import RepositoryQAAdapter, SPLRepositoryQAAdapter
from .skills import FileSandbox, Skill, format_skills_for_prompt


class AgentRuntime(Protocol):
    id: str
    name: str
    role: str
    can_use_skills: bool

    async def respond(self, context: InterviewRoundContext, prompt: str | None = None) -> ChatMessage:
        ...


class InterviewerSkillAgent:
    def __init__(
        self,
        llm: LLMServices,
        skills: list[Skill],
        sandbox: FileSandbox,
        session_id: str,
    ):
        self.id = "interviewer"
        self.name = "系统访谈者"
        self.role = "interviewer"
        self.can_use_skills = True
        self.llm = llm
        self.skills = skills
        self.sandbox = sandbox
        self.session_id = session_id
        self.skill_root = Path(skills[0].location).resolve()
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
                    "name": "run_skill_script",
                    "description": (
                        "Run one built-in requirements-elicitation script for framework persistence. "
                        "Use persist_framework_state with action=save/load or clear_framework_state with action=clear."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "script_name": {
                                "type": "string",
                                "enum": ["persist_framework_state", "clear_framework_state"],
                            },
                            "action": {
                                "type": "string",
                                "enum": ["save", "load", "clear"],
                            },
                            "session_id": {"type": "string"},
                            "framework_json": {"type": "string"},
                        },
                        "required": ["script_name", "action", "session_id"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
        ]

    def _run_skill_script(
        self,
        *,
        script_name: str,
        action: str,
        session_id: str,
        framework_json: str | None = None,
    ) -> str:
        script_file = self.skill_root / "scripts" / f"{script_name}.py"
        if script_name not in {"persist_framework_state", "clear_framework_state"}:
            return "TOOL_ERROR: unsupported script_name"
        if not script_file.exists():
            return f"TOOL_ERROR: script missing: {script_file.as_posix()}"
        cmd = [sys.executable, str(script_file), "--action", action, "--session-id", session_id]
        if framework_json is not None and framework_json.strip():
            cmd += ["--framework-json", framework_json]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            detail = proc.stderr.strip() or proc.stdout.strip()
            return f"TOOL_ERROR: script failed: {detail}"
        return proc.stdout.strip() or '{"ok": true}'

    def _build_system_prompt(self) -> str:
        return (
            "你是一个会使用 skills 的会话代理。"
            "当前任务是需求访谈，必须优先使用 requirements-elicitation skill。"
            "行为约束、访谈流程、结束条件都以 skill 内容为准，不要自创规则。"
            "读取文件时只允许读取 SKILL.md 或 SKILL.md 明确引用的路径，不要猜测诸如 config.json 这类未声明文件。"
            "若 skill 需要持久化，请严格按照 skill 文档中定义的脚本与步骤执行。"
            f"当前会话ID是 {self.session_id}。"
            "当完成条件满足时，输出最终结果并在末尾附加 [[INTERVIEW_COMPLETE]]。"
            "访谈进行中时每轮只输出一段短句，不超过120字，默认只问一个关键问题。"
            "你可以用 read_file 工具读取技能目录内容。"
            "\n可用 skills:\n"
            + format_skills_for_prompt(self.skills)
        )

    async def _chat_with_tools(self, messages: list[dict[str, Any]]) -> str:
        for _ in range(99):
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
                            content_text, resolved_path = self.sandbox.read_text(file_path)
                            tool_output = json.dumps(
                                {
                                    "ok": True,
                                    "resolved_path": resolved_path,
                                    "content": content_text,
                                },
                                ensure_ascii=False,
                            )
                    elif tool_name == "run_skill_script":
                        script_name = str(arguments.get("script_name", "")).strip()
                        action = str(arguments.get("action", "")).strip()
                        session_id = str(arguments.get("session_id", "")).strip()
                        framework_json = arguments.get("framework_json")
                        if not script_name or not action:
                            tool_output = "TOOL_ERROR: missing script_name or action"
                        elif not session_id:
                            tool_output = "TOOL_ERROR: missing session_id"
                        else:
                            tool_output = self._run_skill_script(
                                script_name=script_name,
                                action=action,
                                session_id=session_id,
                                framework_json=str(framework_json) if framework_json is not None else None,
                            )
                    else:
                        tool_output = f"TOOL_ERROR: unsupported tool: {tool_name}"
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.get("id", ""),
                        "content": tool_output,
                    }
                )
        raise RuntimeError("LLM returned no content after tool-calling loop")

    async def respond(self, context: InterviewRoundContext, prompt: str | None = None) -> ChatMessage:
        transcript = "\n".join(
            [f"{item.agent_name}({item.role}): {item.text}" for item in context.transcript[-30:]]
        )
        if prompt is None:
            raise ValueError("prompt is required for InterviewerSkillAgent.respond")
        messages = [
            {"role": "system", "content": self._build_system_prompt()},
            {
                "role": "user",
                "content": (
                    f"当前第 {context.round_index} 轮。\n"
                    f"会话状态：{context.metadata['session_status']}\n"
                    f"会话ID：{context.metadata['session_id']}\n"
                    f"上下文对话：\n{transcript}\n"
                    f"当前任务：{prompt}\n"
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
        repository_qa: RepositoryQAAdapter | None = None,
    ):
        self.id = agent_id
        self.name = name
        self.role = "respondent"
        self.can_use_skills = False
        self.github_repo_url = github_repo_url
        self.repository_qa = repository_qa or SPLRepositoryQAAdapter(
            llm_config=llm_config,
            workspace_root=workspace_root,
            github_repo_url=github_repo_url,
            project_name=project_name,
        )

    async def respond(self, context: InterviewRoundContext, prompt: str | None = None) -> ChatMessage:
        transcript = "\n".join([f"{item.agent_name}({item.role}): {item.text}" for item in context.transcript[-20:]])
        if prompt is None:
            raise ValueError("prompt is required for SPLRespondentAgent.respond")
        question = (

            f"系统代理提问：{prompt}\n"
            f"最近对话：\n{transcript}\n"
            "请基于仓库实际结构给出直接回答，优先输出可验证的模块、函数、流程和约束。"
        )
        text = await self.repository_qa.answer(question)
        return ChatMessage(
            id=str(uuid.uuid4()),
            agent_id=self.id,
            agent_name=self.name,
            role=self.role,
            text=text,
            round_index=context.round_index,
        )
