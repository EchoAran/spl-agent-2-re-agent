from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any


def _state_root() -> Path:
    return Path(tempfile.gettempdir()) / "requirements_elicitation_state"


def _state_file(session_id: str) -> Path:
    safe = "".join(ch for ch in session_id if ch.isalnum() or ch in ("-", "_"))
    return _state_root() / f"{safe or 'default'}.json"


def _clear(session_id: str) -> dict[str, Any]:
    target = _state_file(session_id)
    existed = target.exists()
    if existed:
        target.unlink()
    return {"ok": True, "action": "clear", "session_id": session_id, "deleted": existed}


def main() -> None:
    parser = argparse.ArgumentParser(description="Clear persisted requirements framework state.")
    parser.add_argument("--action", choices=["clear"], required=True)
    parser.add_argument("--session-id", required=True)
    args = parser.parse_args()
    result = _clear(args.session_id)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
