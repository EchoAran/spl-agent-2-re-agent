from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any


def _state_root() -> Path:
    root = Path(tempfile.gettempdir()) / "requirements_elicitation_state"
    root.mkdir(parents=True, exist_ok=True)
    return root


def _state_file(session_id: str) -> Path:
    safe = "".join(ch for ch in session_id if ch.isalnum() or ch in ("-", "_"))
    return _state_root() / f"{safe or 'default'}.json"


def _save(session_id: str, framework_json: str) -> dict[str, Any]:
    if not framework_json.strip():
        raise ValueError("framework_json is required for save action")
    data = json.loads(framework_json)
    target = _state_file(session_id)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"ok": True, "action": "save", "session_id": session_id, "file_path": target.as_posix()}


def _load(session_id: str) -> dict[str, Any]:
    target = _state_file(session_id)
    if not target.exists():
        return {
            "ok": True,
            "action": "load",
            "session_id": session_id,
            "exists": False,
            "framework": None,
        }
    data = json.loads(target.read_text(encoding="utf-8"))
    return {
        "ok": True,
        "action": "load",
        "session_id": session_id,
        "exists": True,
        "file_path": target.as_posix(),
        "framework": data,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Persist or load requirements framework state.")
    parser.add_argument("--action", choices=["save", "load"], required=True)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--framework-json", default="")
    args = parser.parse_args()

    if args.action == "save":
        result = _save(args.session_id, args.framework_json)
    else:
        result = _load(args.session_id)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
