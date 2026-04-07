from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Skill:
    name: str
    description: str
    location: str
    skill_md_path: str


def parse_skill_md(skill_md_path: Path) -> Skill | None:
    try:
        content = skill_md_path.read_text(encoding="utf-8")
    except OSError:
        return None

    if not content.startswith("---"):
        return None

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None

    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None

    name = str(meta.get("name", "")).strip()
    description = str(meta.get("description", "")).strip()
    if not name or not description:
        return None

    skill_dir = skill_md_path.parent.resolve()
    return Skill(
        name=name,
        description=description,
        location=skill_dir.as_posix(),
        skill_md_path=skill_md_path.resolve().as_posix(),
    )


def scan_skills(skill_roots: list[Path]) -> list[Skill]:
    found: dict[str, Skill] = {}
    for root in skill_roots:
        if not root.exists() or not root.is_dir():
            continue
        for child in sorted(root.iterdir()):
            if not child.is_dir():
                continue
            skill_md_path = child / "SKILL.md"
            if not skill_md_path.exists():
                continue
            skill = parse_skill_md(skill_md_path)
            if skill:
                found[skill.name] = skill
    return sorted(found.values(), key=lambda item: item.name)


def xml_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def format_skills_for_prompt(skills: list[Skill]) -> str:
    if not skills:
        return "<available_skills></available_skills>"

    items = []
    for skill in skills:
        items.append(
            "\n".join(
                [
                    "  <skill>",
                    f"    <name>{xml_escape(skill.name)}</name>",
                    f"    <description>{xml_escape(skill.description)}</description>",
                    f"    <location>{xml_escape(skill.location)}</location>",
                    "  </skill>",
                ]
            )
        )
    return "<available_skills>\n" + "\n".join(items) + "\n</available_skills>"


class FileSandbox:
    def __init__(self, allowed_roots: list[Path], skills: list[Skill]) -> None:
        self.allowed_roots = [item.resolve() for item in allowed_roots]
        self.skills = skills

    def _is_allowed(self, path: Path) -> bool:
        resolved = path.resolve()
        for root in self.allowed_roots:
            try:
                resolved.relative_to(root)
                return True
            except ValueError:
                continue
        return False

    def _resolve_path(self, file_path: str) -> Path:
        normalized = file_path.replace("\\", "/")
        path = Path(normalized)
        if path.is_absolute():
            return path.resolve()
        return (Path.cwd() / path).resolve()

    def _find_skill_root(self, path: Path) -> Path | None:
        resolved = path.resolve()
        for skill in self.skills:
            skill_root = Path(skill.location)
            try:
                resolved.relative_to(skill_root)
                return skill_root
            except ValueError:
                continue
        return None

    def read_text(self, file_path: str) -> tuple[str, str]:
        path = self._resolve_path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not self._is_allowed(path):
            raise PermissionError(f"Access denied: {file_path}")

        content = path.read_text(encoding="utf-8")
        skill_root = self._find_skill_root(path)
        base_dir = skill_root.as_posix() if skill_root else path.parent.resolve().as_posix()
        content = content.replace("{baseDir}", base_dir)
        return content, path.resolve().as_posix()
