from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List

from .config import LLMConfig
from .llm_runtime import create_openai_client
from .models import SPLTree
from .tools import SPLToolset


SYSTEM_PROTOCOL = {
    "role": "system_controller",
    "task": "answer questions about a Python code project by navigating an SPL semantic tree",
    "rules": [
        "You cannot inspect source code directly. Only use the provided SPL tools.",
        "SPL is structured as project -> modules -> functions -> fields.",
        "Prefer minimal retrieval. Start from overview and summary before requesting detailed flows.",
        "For macro questions, start with get_project_overview or get_module_overview.",
        "When the target function is unknown, use find_functions first.",
        "When you need process relationships, prefer trace_call_graph before pulling full flows.",
        "Use get_function_field or get_function_spl_fragment for partial retrieval instead of loading a whole function.",
        "Return JSON only.",
    ],
    "response_schema": {
        "tool": {
            "action": "tool",
            "tool_name": "one registered tool name",
            "arguments": {"tool_argument": "value"},
            "notes": "short planning note",
        },
        "tool_batch": {
            "action": "tool_batch",
            "calls": [
                {
                    "tool_name": "registered tool",
                    "arguments": {"tool_argument": "value"},
                }
            ],
            "notes": "short planning note",
        },
        "final": {
            "action": "final",
            "answer": "final user-facing answer only",
        },
    },
}


@dataclass
class AgentTrace:
    round_index: int
    tool_name: str
    arguments: Dict[str, Any]
    result: Dict[str, Any]


@dataclass
class AgentResult:
    answer: str
    rounds: int
    traces: List[AgentTrace] = field(default_factory=list)
    stopped_by_limit: bool = False


class SPLAgentLoop:
    def __init__(self, llm_config: LLMConfig, max_rounds: int = 15):
        if not llm_config.enabled:
            raise ValueError("LLM configuration is required for agent loop execution")
        self.llm_config = llm_config
        self.max_rounds = max_rounds
        self.client, self.llm_config = create_openai_client(llm_config)

    def answer(self, tree: SPLTree, question: str) -> AgentResult:
        toolset = SPLToolset(tree)
        tool_map = {
            "get_project_overview": toolset.get_project_overview,
            "inspect_children": toolset.inspect_children,
            "find_functions": toolset.find_functions,
            "get_module_overview": toolset.get_module_overview,
            "get_function_overview": toolset.get_function_overview,
            "trace_call_graph": toolset.trace_call_graph,
            "get_function_field": toolset.get_function_field,
            "get_flow_steps": toolset.get_flow_steps,
            "get_function_spl_fragment": toolset.get_function_spl_fragment,
            "get_calls": toolset.get_calls,
            "get_callers": toolset.get_callers,
            "get_node": toolset.get_node,
        }

        messages: List[Dict[str, str]] = [
            {"role": "system", "content": json.dumps(self._system_payload(), ensure_ascii=False)},
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "type": "question",
                        "project": {
                            "project_name": tree.project_name,
                            "module_count": len([node for node in tree.iter_nodes() if node.node_type == "module"]),
                            "function_count": len(tree.function_nodes()),
                        },
                        "question": question,
                    },
                    ensure_ascii=False,
                ),
            },
        ]
        traces: List[AgentTrace] = []

        for round_index in range(1, self.max_rounds + 1):
            payload = self._request_json_response(messages)
            messages.append({"role": "assistant", "content": json.dumps(payload, ensure_ascii=False)})
            action = str(payload.get("action") or "").strip()

            if action == "final":
                return AgentResult(answer=str(payload.get("answer") or ""), rounds=round_index, traces=traces)

            calls = self._extract_calls(payload)
            if not calls:
                messages.append(
                    {
                        "role": "user",
                        "content": json.dumps(
                            {
                                "type": "tool_result",
                                "ok": False,
                                "error": "Invalid agent response. Return action=tool, action=tool_batch, or action=final.",
                            },
                            ensure_ascii=False,
                        ),
                    }
                )
                continue

            tool_results: List[Dict[str, Any]] = []
            for call in calls:
                tool_name = call["tool_name"]
                arguments = call["arguments"]
                tool_fn = tool_map.get(tool_name)
                if tool_fn is None:
                    result = {"ok": False, "error": f"Unknown tool: {tool_name}"}
                else:
                    try:
                        result = tool_fn(**arguments)
                    except Exception as exc:
                        result = {"ok": False, "error": str(exc)}
                traces.append(
                    AgentTrace(
                        round_index=round_index,
                        tool_name=tool_name,
                        arguments=arguments,
                        result=result,
                    )
                )
                tool_results.append(
                    {
                        "tool_name": tool_name,
                        "arguments": arguments,
                        "result": result,
                    }
                )

            messages.append(
                {
                    "role": "user",
                    "content": json.dumps(
                        {
                            "type": "tool_result",
                            "tool_results": tool_results,
                        },
                        ensure_ascii=False,
                    ),
                }
            )

        return AgentResult(
            answer="Stopped because the maximum agent loop rounds were reached before a final answer was produced.",
            rounds=self.max_rounds,
            traces=traces,
            stopped_by_limit=True,
        )

    def _system_payload(self) -> Dict[str, Any]:
        return {
            **SYSTEM_PROTOCOL,
            "tools": SPLToolset.tool_definitions(),
            "strategy": [
                "For high-level project questions, start from project or module overview.",
                "For function localization, use find_functions and then get_function_overview.",
                "For call-chain questions, trace the call graph before opening flow details.",
                "For process explanations, request only the steps you need.",
                "Do not fetch full raw_spl unless explicitly required.",
            ],
        }

    def _request_json_response(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        response = self.client.chat.completions.create(
            model=self.llm_config.model,
            messages=messages,
            temperature=self.llm_config.temperature,
            timeout=self.llm_config.timeout_sec,
        )
        text = response.choices[0].message.content or ""
        return json.loads(self._extract_json_payload(text))

    def _extract_json_payload(self, text: str) -> str:
        s = (text or "").strip()
        if not s:
            raise ValueError("LLM returned empty output")
        first_obj = s.find("{")
        if first_obj != -1:
            depth = 0
            in_string = False
            escape = False
            for index in range(first_obj, len(s)):
                char = s[index]
                if escape:
                    escape = False
                    continue
                if char == "\\":
                    escape = True
                    continue
                if char == '"':
                    in_string = not in_string
                    continue
                if in_string:
                    continue
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        return s[first_obj:index + 1]
        raise ValueError("No JSON object found in LLM output")

    def _extract_calls(self, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        action = str(payload.get("action") or "")
        if action == "tool":
            tool_name = str(payload.get("tool_name") or "").strip()
            arguments = payload.get("arguments") or {}
            if not tool_name or not isinstance(arguments, dict):
                return []
            return [{"tool_name": tool_name, "arguments": arguments}]
        if action == "tool_batch":
            calls = payload.get("calls") or []
            normalized: List[Dict[str, Any]] = []
            for call in calls[:3]:
                if not isinstance(call, dict):
                    continue
                tool_name = str(call.get("tool_name") or "").strip()
                arguments = call.get("arguments") or {}
                if tool_name and isinstance(arguments, dict):
                    normalized.append({"tool_name": tool_name, "arguments": arguments})
            return normalized
        return []
