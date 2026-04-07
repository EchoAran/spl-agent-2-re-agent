from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

import aiohttp

from .models import LLMConfig


class ApplicationError(Exception):
    def __init__(self, message: str, non_retryable: bool = False):
        super().__init__(message)
        self.non_retryable = non_retryable


logger = logging.getLogger("multi_agent_interview.llm")


def load_llm_config(env_file_path: Path | None = None) -> LLMConfig:
    env_values: dict[str, str] = {}
    if env_file_path and env_file_path.exists():
        for line in env_file_path.read_text(encoding="utf-8").splitlines():
            raw = line.strip()
            if not raw or raw.startswith("#") or "=" not in raw:
                continue
            key, value = raw.split("=", 1)
            env_values[key.strip()] = value.strip().strip('"').strip("'")

    base_url = os.getenv("BASE_URL") or env_values.get("BASE_URL", "")
    api_key = os.getenv("API_KEY") or env_values.get("API_KEY", "")
    model = os.getenv("MODEL") or env_values.get("MODEL", "gpt-5")
    if not base_url or not api_key:
        raise ValueError("missing BASE_URL or API_KEY in environment/.env")
    return LLMConfig(base_url=base_url, api_key=api_key, model=model)


class LLMServices:
    def __init__(self, session: aiohttp.ClientSession, config: LLMConfig):
        self.session = session
        self.config = config

    async def chat(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        tool_choice: str | dict[str, Any] | None = None,
        temperature: float = 0,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "model": self.config.model,
            "messages": messages,
            "temperature": temperature,
            "stream": False,
        }
        if tools:
            payload["tools"] = tools
        if tools and tool_choice is not None:
            payload["tool_choice"] = tool_choice
        request_preview = {
            "url": self.config.base_url.rstrip("/") + "/v1/chat/completions",
            "model": payload.get("model"),
            "temperature": payload.get("temperature"),
            "message_count": len(messages),
            "tools_count": len(tools) if tools else 0,
            "has_tool_choice": "tool_choice" in payload,
            "last_message_preview": str(messages[-1].get("content", ""))[:300] if messages else "",
        }
        logger.info("llm_request %s", json.dumps(request_preview, ensure_ascii=False))

        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
        }

        async with self.session.post(
            self.config.base_url.rstrip("/") + "/v1/chat/completions",
            json=payload,
            headers=headers,
        ) as response:
            body_text = await response.text()
            logger.info(
                "llm_response status=%s body_preview=%s",
                response.status,
                body_text[:1200],
            )
            if response.status >= 400:
                raise ApplicationError(
                    f"HTTP Error {response.status}: {body_text}",
                    non_retryable=response.status < 500,
                )
            data = json.loads(body_text)

        choice = data.get("choices", [])[0]
        message = choice.get("message", {})
        finish_reason = choice.get("finish_reason")

        content = message.get("content")
        if isinstance(content, list):
            text_parts: list[str] = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(str(item.get("text", "")))
                else:
                    text_parts.append(str(item))
            message["content"] = "\n".join(text_parts)
        elif content is None:
            message["content"] = ""
        elif not isinstance(content, str):
            message["content"] = str(content)

        return {
            "message": message,
            "finish_reason": finish_reason,
            "raw": data,
        }
