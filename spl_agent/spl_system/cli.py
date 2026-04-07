from __future__ import annotations

import argparse

import uvicorn

from run_from_config import main as run_from_config_main
from spl_system.api.app import create_app


def run() -> None:
    run_from_config_main()


def serve() -> None:
    parser = argparse.ArgumentParser(description="Run the SPL Code Understanding HTTP API.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--reload", action="store_true")
    parser.add_argument("--config", default="settings.yaml")
    args = parser.parse_args()

    app = create_app(args.config)
    uvicorn.run(app, host=args.host, port=args.port, reload=args.reload)


def main() -> None:
    parser = argparse.ArgumentParser(description="SPL-centered code understanding toolkit.")
    parser.add_argument("command", choices=["run", "serve"], nargs="?", default="run")
    args, _ = parser.parse_known_args()
    if args.command == "serve":
        serve()
    else:
        run()
