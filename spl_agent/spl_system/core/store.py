from __future__ import annotations

from pathlib import Path
from typing import Optional
import json

from .models import SPLTree, stable_hash


class SPLStore:
    def __init__(self, cache_dir: str | Path):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def git_project_dir(self, normalized_url: str, commit: str) -> Path:
        return self.cache_dir / "git" / stable_hash(normalized_url) / commit

    def local_project_dir(self, local_path: str) -> Path:
        return self.cache_dir / "local" / stable_hash(str(Path(local_path).resolve()))

    def project_dir(self, source_type: str, source_key: str, commit: Optional[str] = None) -> Path:
        if source_type == "git":
            if not commit:
                raise ValueError("commit is required for git project storage")
            return self.git_project_dir(source_key, commit)
        return self.local_project_dir(source_key)

    def spl_tree_path(self, source_type: str, source_key: str, commit: Optional[str] = None) -> Path:
        return self.project_dir(source_type, source_key, commit) / "spl_tree.json"

    def exports_dir(self, source_type: str, source_key: str, commit: Optional[str] = None) -> Path:
        return self.project_dir(source_type, source_key, commit) / "exports"

    def source_meta_path(self, source_type: str, source_key: str, commit: Optional[str] = None) -> Path:
        return self.project_dir(source_type, source_key, commit) / "source_meta.json"

    def has_tree(self, source_type: str, source_key: str, commit: Optional[str] = None) -> bool:
        return self.spl_tree_path(source_type, source_key, commit).exists()

    def load_tree(self, source_type: str, source_key: str, commit: Optional[str] = None) -> SPLTree:
        path = self.spl_tree_path(source_type, source_key, commit)
        return SPLTree.from_json(path.read_text(encoding="utf-8"))

    def save_tree(
        self,
        tree: SPLTree,
        source_type: str,
        source_key: str,
        commit: Optional[str] = None,
        source_meta: Optional[dict] = None,
    ) -> Path:
        project_dir = self.project_dir(source_type, source_key, commit)
        project_dir.mkdir(parents=True, exist_ok=True)
        path = self.spl_tree_path(source_type, source_key, commit)
        path.write_text(tree.to_json(), encoding="utf-8")
        if source_meta is not None:
            self.source_meta_path(source_type, source_key, commit).write_text(
                json.dumps(source_meta, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        return path

