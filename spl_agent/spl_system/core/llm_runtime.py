from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple

from openai import OpenAI

from .config import AppConfig, LLMConfig


def resolve_config_path(config_path: str | Path | None = None) -> Path:
    if config_path is not None:
        return Path(config_path)
    env_path = os.getenv("SPL_CONFIG_PATH")
    if env_path:
        return Path(env_path)
    return Path("settings.yaml")


def load_runtime_llm_config(config_path: str | Path | None = None) -> LLMConfig:
    path = resolve_config_path(config_path)
    if path.exists():
        return AppConfig.load(path).llm
    return LLMConfig()


def create_openai_client(
    llm_config: Optional[LLMConfig] = None,
    config_path: str | Path | None = None,
) -> Tuple[OpenAI, LLMConfig]:
    config = llm_config or load_runtime_llm_config(config_path)
    base_url = (config.base_url or "").rstrip("/")
    if base_url and not base_url.endswith("/v1"):
        base_url = f"{base_url}/v1"
    normalized = config.model_copy(update={"base_url": base_url or config.base_url})
    return OpenAI(api_key=normalized.api_key, base_url=normalized.base_url), normalized
