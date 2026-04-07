from __future__ import annotations

from pathlib import Path
import re
from typing import Literal, Optional

import yaml
from pydantic import BaseModel, Field, model_validator


class LLMConfig(BaseModel):
    api_key: str = Field(default="", description="LLM API key")
    base_url: str = Field(default="https://api.rcouyi.com/v1")
    model: str = Field(default="gpt-5")
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)
    timeout_sec: int = Field(default=120, ge=5)

    @property
    def enabled(self) -> bool:
        return bool(self.api_key and self.model)


class SourceConfig(BaseModel):
    type: Optional[Literal["git", "local"]] = None
    target: Optional[str] = None
    repo_url: Optional[str] = None
    commit: Optional[str] = None
    local_path: Optional[str] = None
    project_name: Optional[str] = None
    prefer_legacy_spl: bool = True
    force_rebuild: bool = False

    @model_validator(mode="after")
    def validate_source(self) -> "SourceConfig":
        source_value = (self.target or self.repo_url or self.local_path or "").strip()
        if not source_value:
            raise ValueError("source.target or source.repo_url/source.local_path is required")

        detected_type = self.type or self._detect_source_type(source_value)
        if detected_type == "git":
            self.type = "git"
            self.repo_url = self.repo_url or source_value
            self.local_path = None
        elif detected_type == "local":
            self.type = "local"
            self.local_path = self.local_path or source_value
            self.repo_url = None
        else:
            raise ValueError(f"Unsupported source type: {detected_type}")

        self.target = source_value
        return self

    def _detect_source_type(self, value: str) -> str:
        text = value.strip()
        if re.match(r"^(https?://|git@)", text) or text.endswith(".git"):
            return "git"
        return "local"


class RuntimeConfig(BaseModel):
    cache_dir: str = ".spl_cache"
    max_rounds: int = Field(default=15, ge=1, le=50)
    build_workers: int = Field(default=4, ge=1, le=32)
    export_spl: bool = True
    use_llm_for_build: bool = True
    tool_timeout_sec: int = Field(default=30, ge=1)


class AppConfig(BaseModel):
    llm: LLMConfig = Field(default_factory=LLMConfig)
    source: SourceConfig
    runtime: RuntimeConfig = Field(default_factory=RuntimeConfig)
    question: str = ""

    @classmethod
    def load(cls, file_path: str | Path) -> "AppConfig":
        path = Path(file_path)
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        data = cls._normalize_legacy_keys(data)
        return cls.model_validate(data)

    @staticmethod
    def _normalize_legacy_keys(data: dict) -> dict:
        normalized = dict(data)

        llm_block = dict(normalized.get("llm") or {})
        if "OpenAI_API_Base" in normalized and "base_url" not in llm_block:
            llm_block["base_url"] = normalized["OpenAI_API_Base"]
        if "API_key_list" in normalized and "api_key" not in llm_block:
            key_list = normalized.get("API_key_list") or []
            if isinstance(key_list, list) and key_list:
                llm_block["api_key"] = str(key_list[0]).strip()
        if "model_name" in normalized and "model" not in llm_block:
            llm_block["model"] = normalized["model_name"]
        if llm_block:
            normalized["llm"] = llm_block

        source_block = dict(normalized.get("source") or {})
        if "project_url" in normalized and "target" not in source_block:
            source_block["target"] = normalized["project_url"]
        if "project_path" in normalized and "target" not in source_block:
            source_block["target"] = normalized["project_path"]
        if "revision" in normalized and "commit" not in source_block:
            source_block["commit"] = normalized["revision"]
        if "project_name" in normalized and "project_name" not in source_block:
            source_block["project_name"] = normalized["project_name"]
        if source_block:
            normalized["source"] = source_block

        if "user_question" in normalized and "question" not in normalized:
            normalized["question"] = normalized["user_question"]
        return normalized
