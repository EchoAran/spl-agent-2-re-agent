from __future__ import annotations

import asyncio
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Protocol

from .models import LLMConfig


class RepositoryQAAdapter(Protocol):
    async def answer(self, question: str) -> str:
        ...


class SPLRepositoryQAAdapter:
    def __init__(
        self,
        *,
        llm_config: LLMConfig,
        workspace_root: Path,
        github_repo_url: str,
        project_name: str | None = None,
    ) -> None:
        self.llm_config = llm_config
        self.workspace_root = workspace_root.resolve()
        self.github_repo_url = github_repo_url
        self.project_name = project_name
        self._service: Any = None
        self._project_id: str | None = None
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

        llm_io_path = self.workspace_root / "backend" / "runtime" / "llm_io.jsonl"
        llm_io_path.parent.mkdir(parents=True, exist_ok=True)
        os.environ["SPL_LLM_IO_LOG_PATH"] = str(llm_io_path)

        cache_dir_env = os.getenv("SPL_INTERVIEW_CACHE_DIR", "").strip()
        if cache_dir_env:
            cache_dir = Path(cache_dir_env).expanduser()
        else:
            # Keep cache root short on Windows to avoid path-length issues during git checkout.
            cache_dir = Path(tempfile.gettempdir()) / "spl_i"
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

    async def answer(self, question: str) -> str:
        await self._ensure_project_ready()
        project_id = self._project_id or ""
        result = await asyncio.to_thread(self._service_instance().ask, project_id, question)
        return str(result.answer).strip()
