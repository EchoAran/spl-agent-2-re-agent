from __future__ import annotations

from pathlib import Path
import re
import subprocess
from typing import Optional

from .models import SourceHandle, stable_hash


class SourceResolver:
    def __init__(self, cache_dir: str | Path):
        self.cache_dir = Path(cache_dir)
        self.git_sources_dir = self.cache_dir / "git_sources"
        self.checkouts_dir = self.cache_dir / "checkouts"
        self.git_sources_dir.mkdir(parents=True, exist_ok=True)
        self.checkouts_dir.mkdir(parents=True, exist_ok=True)

    def normalize_git_url(self, repo_url: str) -> str:
        text = repo_url.strip()
        text = text.rstrip("/")
        text = re.sub(r"\.git$", "", text)
        return text

    def resolve_local(self, local_path: str, project_name: Optional[str] = None) -> SourceHandle:
        root = Path(local_path).resolve()
        if not root.exists():
            raise FileNotFoundError(f"Local path does not exist: {root}")
        name = project_name or root.name
        cache_key = str(root)
        project_id = f"local:{stable_hash(cache_key)[:16]}"
        return SourceHandle(
            source_type="local",
            display_name=name,
            project_root=root,
            cache_key=cache_key,
            project_id=project_id,
            normalized_source=cache_key,
            metadata={"local_path": str(root)},
        )

    def resolve_git(
        self,
        repo_url: str,
        commit: Optional[str] = None,
        project_name: Optional[str] = None,
    ) -> SourceHandle:
        normalized_url = self.normalize_git_url(repo_url)
        source_hash = stable_hash(normalized_url)
        mirror_dir = self.git_sources_dir / source_hash

        if mirror_dir.exists():
            self._run_git(["git", "--git-dir", str(mirror_dir), "fetch", "--all", "--tags"])
        else:
            self._run_git(["git", "clone", "--mirror", repo_url.strip(), str(mirror_dir)])

        requested_ref = commit or "HEAD"
        resolved_commit = self._resolve_commit(mirror_dir, commit)
        checkout_dir = self.checkouts_dir / source_hash / resolved_commit
        if not checkout_dir.exists():
            checkout_dir.parent.mkdir(parents=True, exist_ok=True)
            self._run_git(["git", "clone", str(mirror_dir), str(checkout_dir)])
            self._run_git(["git", "-C", str(checkout_dir), "checkout", resolved_commit])

        name = project_name or Path(normalized_url).name or resolved_commit[:8]
        project_id = f"git:{source_hash[:16]}:{resolved_commit[:12]}"
        return SourceHandle(
            source_type="git",
            display_name=name,
            project_root=checkout_dir,
            cache_key=normalized_url,
            project_id=project_id,
            normalized_source=normalized_url,
            commit=resolved_commit,
            metadata={
                "repo_url": repo_url,
                "normalized_repo_url": normalized_url,
                "checkout_dir": str(checkout_dir),
                "requested_ref": requested_ref,
                "resolved_commit": resolved_commit,
            },
        )

    def _resolve_commit(self, mirror_dir: Path, requested_commit: Optional[str]) -> str:
        ref = requested_commit or "HEAD"
        result = self._run_git(["git", "--git-dir", str(mirror_dir), "rev-parse", ref])
        return result.strip()

    def _run_git(self, command: list[str]) -> str:
        proc = subprocess.run(command, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            stderr = proc.stderr.strip() or proc.stdout.strip()
            raise RuntimeError(f"Git command failed: {' '.join(command)}\n{stderr}")
        return proc.stdout.strip()
