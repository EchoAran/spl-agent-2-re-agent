from __future__ import annotations

import argparse
import json
from pathlib import Path

from spl_system.core.config import AppConfig
from spl_system.core.service import SPLProjectService


def main() -> None:
    parser = argparse.ArgumentParser(description="Run SPL code understanding from a config file.")
    parser.add_argument("--config", default="settings.yaml", help="Path to the YAML config file.")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    config = AppConfig.load(config_path)
    service = SPLProjectService.from_config(config, base_dir=Path(__file__).resolve().parent)
    if config.question.strip() and config.llm.enabled:
        query_result = service.query(
            question=config.question,
            source_type=config.source.type,
            target=config.source.target,
            repo_url=config.source.repo_url,
            commit=config.source.commit,
            local_path=config.source.local_path,
            project_name=config.source.project_name,
            prefer_legacy_spl=config.source.prefer_legacy_spl,
            force_rebuild=config.source.force_rebuild,
            use_llm_for_build=config.runtime.use_llm_for_build,
            export_spl=config.runtime.export_spl,
        )
        print(json.dumps({k: v for k, v in query_result.items() if k != "tool_trace" and k != "answer"}, ensure_ascii=False, indent=2))
        print("\n=== FINAL ANSWER ===")
        print(query_result["answer"])
    else:
        build_result = service.build_project(
            source_type=config.source.type,
            target=config.source.target,
            repo_url=config.source.repo_url,
            commit=config.source.commit,
            local_path=config.source.local_path,
            project_name=config.source.project_name,
            prefer_legacy_spl=config.source.prefer_legacy_spl,
            force_rebuild=config.source.force_rebuild,
            use_llm_for_build=config.runtime.use_llm_for_build,
            export_spl=config.runtime.export_spl,
        )
        print(json.dumps(build_result, ensure_ascii=False, indent=2))
    if config.question.strip() and not config.llm.enabled:
        print("\n=== NOTE ===")
        print("LLM is not configured, so the project was built but the question was not executed.")


if __name__ == "__main__":
    main()
