from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from .agent_loop import AgentResult, SPLAgentLoop
from .builder import ProjectSPLBuilder
from .config import AppConfig, LLMConfig
from .models import SPLTree
from .semantic_builder import FunctionSemanticBuilder
from .sources import SourceResolver
from .store import SPLStore


class SPLProjectService:
    def __init__(
        self,
        base_dir: str | Path,
        llm_config: LLMConfig,
        cache_dir: str | Path,
        max_rounds: int = 15,
        build_workers: int = 4,
    ):
        self.base_dir = Path(base_dir)
        self.store = SPLStore(cache_dir)
        self.sources = SourceResolver(cache_dir)
        self.semantic_builder = FunctionSemanticBuilder(llm_config=llm_config, base_dir=self.base_dir)
        self.builder = ProjectSPLBuilder(self.semantic_builder, max_workers=build_workers)
        self.llm_config = llm_config
        self.max_rounds = max_rounds
        self._tree_cache: Dict[str, SPLTree] = {}

    @classmethod
    def from_config(cls, config: AppConfig, base_dir: str | Path) -> "SPLProjectService":
        return cls(
            base_dir=base_dir,
            llm_config=config.llm,
            cache_dir=config.runtime.cache_dir,
            max_rounds=config.runtime.max_rounds,
            build_workers=config.runtime.build_workers,
        )

    def build_project(
        self,
        source_type: Optional[str] = None,
        target: Optional[str] = None,
        repo_url: Optional[str] = None,
        commit: Optional[str] = None,
        local_path: Optional[str] = None,
        project_name: Optional[str] = None,
        prefer_legacy_spl: bool = True,
        force_rebuild: bool = False,
        use_llm_for_build: bool = True,
        export_spl: bool = True,
    ) -> Dict[str, Any]:
        source_value = target or repo_url or local_path or ""
        resolved_source_type = source_type or ("git" if source_value.startswith(("http://", "https://", "git@")) or source_value.endswith(".git") else "local")

        if resolved_source_type == "git":
            handle = self.sources.resolve_git(
                repo_url=repo_url or target or "",
                commit=commit,
                project_name=project_name,
            )
            source_key = handle.normalized_source
            store_commit = handle.commit
        elif resolved_source_type == "local":
            handle = self.sources.resolve_local(local_path=local_path or target or "", project_name=project_name)
            source_key = handle.normalized_source
            store_commit = None
        else:
            raise ValueError(f"Unsupported source type: {resolved_source_type}")

        cache_hit = False
        if not force_rebuild and self.store.has_tree(handle.source_type, source_key, store_commit):
            tree = self.store.load_tree(handle.source_type, source_key, store_commit)
            cache_hit = True
        else:
            legacy_root = self.builder.discover_legacy_root(handle.project_root) if prefer_legacy_spl else None
            if legacy_root is not None:
                tree = self.builder.build_from_legacy(handle, legacy_root)
            else:
                tree, exported_spl = self.builder.build_from_source(handle, use_llm=use_llm_for_build)
                if export_spl:
                    self.builder.export_spl_files(
                        exported_spl,
                        self.store.exports_dir(handle.source_type, source_key, store_commit),
                    )
            self.store.save_tree(
                tree,
                handle.source_type,
                source_key,
                store_commit,
                source_meta={
                    "project_id": handle.project_id,
                    "project_root": str(handle.project_root),
                    "source_type": handle.source_type,
                    "normalized_source": handle.normalized_source,
                    "commit": handle.commit,
                },
            )

        self._tree_cache[handle.project_id] = tree
        return {
            "project_id": handle.project_id,
            "project_name": tree.project_name,
            "cache_hit": cache_hit,
            "source_type": handle.source_type,
            "normalized_source": handle.normalized_source,
            "commit": handle.commit,
            "requested_ref": handle.metadata.get("requested_ref"),
            "spl_tree_path": str(self.store.spl_tree_path(handle.source_type, source_key, store_commit)),
        }

    def get_tree(self, project_id: str) -> SPLTree:
        if project_id in self._tree_cache:
            return self._tree_cache[project_id]
        prefix, rest = project_id.split(":", 1)
        if prefix == "git":
            repo_hash, short_commit = rest.split(":", 1)
            git_root = self.store.cache_dir / "git"
            repo_dirs = [path for path in git_root.iterdir() if path.is_dir() and path.name.startswith(repo_hash)] if git_root.exists() else []
            if not repo_dirs:
                raise FileNotFoundError(f"Project not found: {project_id}")
            git_dir = repo_dirs[0]
            matches = [path for path in git_dir.iterdir() if path.is_dir() and path.name.startswith(short_commit)]
            if not matches:
                raise FileNotFoundError(f"Project not found: {project_id}")
            tree = SPLTree.from_json((matches[0] / "spl_tree.json").read_text(encoding="utf-8"))
        else:
            local_hash = rest
            local_root = self.store.cache_dir / "local"
            local_dirs = [path for path in local_root.iterdir() if path.is_dir() and path.name.startswith(local_hash)] if local_root.exists() else []
            if not local_dirs:
                raise FileNotFoundError(f"Project not found: {project_id}")
            tree_path = local_dirs[0] / "spl_tree.json"
            tree = SPLTree.from_json(tree_path.read_text(encoding="utf-8"))
        self._tree_cache[project_id] = tree
        return tree

    def ask(self, project_id: str, question: str) -> AgentResult:
        tree = self.get_tree(project_id)
        agent = SPLAgentLoop(self.llm_config, max_rounds=self.max_rounds)
        return agent.answer(tree, question)

    def query(
        self,
        question: str,
        source_type: Optional[str] = None,
        target: Optional[str] = None,
        repo_url: Optional[str] = None,
        commit: Optional[str] = None,
        local_path: Optional[str] = None,
        project_name: Optional[str] = None,
        prefer_legacy_spl: bool = True,
        force_rebuild: bool = False,
        use_llm_for_build: bool = True,
        export_spl: bool = True,
    ) -> Dict[str, Any]:
        build_result = self.build_project(
            source_type=source_type,
            target=target,
            repo_url=repo_url,
            commit=commit,
            local_path=local_path,
            project_name=project_name,
            prefer_legacy_spl=prefer_legacy_spl,
            force_rebuild=force_rebuild,
            use_llm_for_build=use_llm_for_build,
            export_spl=export_spl,
        )
        result = self.ask(build_result["project_id"], question)
        return {
            "answer": result.answer,
            "project_id": build_result["project_id"],
            "project_name": build_result["project_name"],
            "source_type": build_result["source_type"],
            "normalized_source": build_result["normalized_source"],
            "commit": build_result["commit"],
            "cache_hit": build_result["cache_hit"],
            "rounds": result.rounds,
            "stopped_by_limit": result.stopped_by_limit,
            "tool_trace": [
                {
                    "round": trace.round_index,
                    "tool_name": trace.tool_name,
                    "arguments": trace.arguments,
                    "result": trace.result,
                }
                for trace in result.traces
            ],
        }
