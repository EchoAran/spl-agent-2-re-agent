from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    base_url: str = Field(min_length=1)
    api_key: str = Field(min_length=1)
    model: str = Field(default="gpt-5")


class CreateSessionRequest(BaseModel):
    github_repo_url: str = Field(min_length=1)
    project_name: str | None = None


class SessionResponse(BaseModel):
    session_id: str
    enabled_agent_ids: list[str]
    interviewer_agent_id: str
    status: str


class ClientEvent(BaseModel):
    type: str
    text: str | None = None


class ChatMessageResponse(BaseModel):
    id: str
    agent_id: str
    agent_name: str
    role: str
    text: str
    round_index: int


class SessionStatusResponse(BaseModel):
    session_id: str
    status: str
    reason: str | None = None


class SessionMessagesResponse(BaseModel):
    session_id: str
    interviewer_agent_id: str
    status: str
    reason: str | None = None
    messages: list[ChatMessageResponse] = Field(default_factory=list)


@dataclass
class ChatMessage:
    id: str
    agent_id: str
    agent_name: str
    role: str
    text: str
    round_index: int


@dataclass
class InterviewRoundContext:
    round_index: int
    user_input: str
    transcript: list[ChatMessage]
    enabled_agent_ids: list[str]
    metadata: dict[str, Any] = field(default_factory=dict)
