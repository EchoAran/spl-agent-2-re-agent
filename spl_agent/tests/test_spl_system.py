from __future__ import annotations

import shutil
import unittest
from pathlib import Path
from unittest.mock import patch
from uuid import uuid4

from fastapi.testclient import TestClient

from client import ask_code_project
from spl_system.api.app import create_app
from spl_system.core.agent_loop import SPLAgentLoop
from spl_system.core.config import AppConfig, LLMConfig
from spl_system.core.llm_runtime import load_runtime_llm_config
from spl_system.core.service import SPLProjectService
from spl_system.client import SPLClient
from spl_system.core.tools import SPLToolset


class _FakeMessage:
    def __init__(self, content: str):
        self.content = content


class _FakeChoice:
    def __init__(self, content: str):
        self.message = _FakeMessage(content)


class _FakeResponse:
    def __init__(self, content: str):
        self.choices = [_FakeChoice(content)]


class _FakeCompletions:
    def __init__(self, outputs: list[str]):
        self.outputs = list(outputs)

    def create(self, **_: object) -> _FakeResponse:
        return _FakeResponse(self.outputs.pop(0))


class _FakeChat:
    def __init__(self, outputs: list[str]):
        self.completions = _FakeCompletions(outputs)


class _FakeClient:
    def __init__(self, outputs: list[str]):
        self.chat = _FakeChat(outputs)


class SPLSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_dir = Path(__file__).resolve().parents[1]
        self.temp_dir = self.base_dir / ".test_tmp" / f"spl_system_test_{uuid4().hex[:8]}"
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.addCleanup(lambda: shutil.rmtree(self.temp_dir, ignore_errors=True))

    def _build_code_tree(self):
        service = SPLProjectService(
            base_dir=self.base_dir,
            llm_config=LLMConfig(),
            cache_dir=self.temp_dir / "cache_source",
            max_rounds=5,
            build_workers=2,
        )
        result = service.build_project(
            source_type="local",
            local_path=str(self.base_dir / "Code"),
            project_name="code_only",
            prefer_legacy_spl=False,
            force_rebuild=True,
            use_llm_for_build=False,
            export_spl=True,
        )
        return service, service.get_tree(result["project_id"])

    def test_build_from_legacy_spl(self) -> None:
        service = SPLProjectService(
            base_dir=self.base_dir,
            llm_config=LLMConfig(),
            cache_dir=self.temp_dir / "cache_legacy",
            max_rounds=5,
        )
        result = service.build_project(
            source_type="local",
            local_path=str(self.base_dir),
            project_name="workspace",
            prefer_legacy_spl=True,
            force_rebuild=True,
            use_llm_for_build=False,
            export_spl=True,
        )
        tree = service.get_tree(result["project_id"])
        self.assertEqual(len(tree.function_nodes()), 3)
        paths = sorted(node.path for node in tree.function_nodes())
        self.assertIn("/modules/test.py/function::checkout", paths)

    def test_build_from_source_without_llm_preserves_dependency_context(self) -> None:
        _, tree = self._build_code_tree()
        self.assertEqual(len(tree.function_nodes()), 3)
        tools = SPLToolset(tree)

        found = tools.find_functions("discount")
        self.assertTrue(found["ok"])
        self.assertEqual(found["matches"][0]["qualified_name"], "apply_discount")

        overview = tools.get_function_overview("/modules/test.py/function::checkout")
        self.assertTrue(overview["ok"])
        self.assertGreaterEqual(overview["function"]["dependency_count"], 1)

        analysis_context = tools.get_function_field("/modules/test.py/function::checkout", "analysis_context")
        self.assertTrue(analysis_context["ok"])
        dependency_context = analysis_context["content"]["dependency_context"]
        self.assertEqual(dependency_context[0]["worker_name"], "calc_total")

        calls = tools.get_calls("/modules/test.py/function::calc_total")
        self.assertTrue(calls["ok"])
        self.assertEqual(calls["calls"], ["/modules/test.py/function::apply_discount"])

        trace = tools.trace_call_graph("/modules/test.py/function::checkout", direction="outbound", max_depth=2)
        self.assertTrue(trace["ok"])
        traced_names = {node["qualified_name"] for node in trace["nodes"]}
        self.assertIn("checkout", traced_names)
        self.assertIn("calc_total", traced_names)
        self.assertIn("apply_discount", traced_names)

        fragment = tools.get_function_spl_fragment(
            "/modules/test.py/function::checkout",
            ["summary", "inputs", "analysis_context"],
        )
        self.assertTrue(fragment["ok"])
        self.assertIn("analysis_context", fragment["fragment"]["fields"])

    def test_reload_tree_from_disk(self) -> None:
        cache_dir = self.temp_dir / "cache_reload"
        service = SPLProjectService(
            base_dir=self.base_dir,
            llm_config=LLMConfig(),
            cache_dir=cache_dir,
            max_rounds=5,
        )
        result = service.build_project(
            source_type="local",
            local_path=str(self.base_dir / "Code"),
            project_name="code_only",
            prefer_legacy_spl=False,
            force_rebuild=True,
            use_llm_for_build=False,
            export_spl=False,
        )

        fresh_service = SPLProjectService(
            base_dir=self.base_dir,
            llm_config=LLMConfig(),
            cache_dir=cache_dir,
            max_rounds=5,
        )
        tree = fresh_service.get_tree(result["project_id"])
        self.assertEqual(tree.project_name, "code_only")
        self.assertEqual(len(tree.function_nodes()), 3)

    def test_agent_loop_uses_json_protocol(self) -> None:
        _, tree = self._build_code_tree()
        agent = SPLAgentLoop(
            LLMConfig(api_key="test-key", base_url="https://example.invalid/v1", model="gpt-5"),
            max_rounds=4,
        )
        agent.client = _FakeClient(
            [
                '{"action":"tool","tool_name":"find_functions","arguments":{"query":"discount"}}',
                '{"action":"final","answer":"折扣逻辑由 apply_discount 负责。"}',
            ]
        )
        result = agent.answer(tree, "谁负责折扣逻辑？")
        self.assertEqual(result.answer, "折扣逻辑由 apply_discount 负责。")
        self.assertEqual(result.rounds, 2)
        self.assertEqual(result.traces[0].tool_name, "find_functions")

    def test_config_target_autodetects_local(self) -> None:
        config = AppConfig.model_validate(
            {
                "llm": {},
                "source": {"target": "./Code"},
                "runtime": {},
                "question": "What does this project do?",
            }
        )
        self.assertEqual(config.source.type, "local")
        self.assertEqual(config.source.local_path, "./Code")

    def test_config_target_autodetects_git(self) -> None:
        config = AppConfig.model_validate(
            {
                "llm": {},
                "source": {"target": "https://github.com/kennethreitz/records"},
                "runtime": {},
                "question": "What does this project do?",
            }
        )
        self.assertEqual(config.source.type, "git")
        self.assertEqual(config.source.repo_url, "https://github.com/kennethreitz/records")

    def test_legacy_style_config_keys_are_supported(self) -> None:
        config = AppConfig.load(self.base_dir / "settings.local_order_demo.yaml")
        self.assertEqual(config.llm.base_url, "https://api.rcouyi.com/v1")
        self.assertEqual(config.source.type, "local")
        self.assertEqual(config.source.local_path, "./demo_projects/local_order_demo")
        self.assertTrue(bool(config.question.strip()))

    def test_build_and_qa_share_same_llm_config_source(self) -> None:
        config = AppConfig.load(self.base_dir / "settings.yaml")
        service = SPLProjectService.from_config(config, base_dir=self.base_dir)
        runtime_llm = load_runtime_llm_config(self.base_dir / "settings.yaml")

        self.assertEqual(service.llm_config.api_key, runtime_llm.api_key)
        self.assertEqual(service.llm_config.base_url, runtime_llm.base_url)
        self.assertEqual(service.semantic_builder.llm_config.model, service.llm_config.model)
        self.assertEqual(service.semantic_builder.llm_config.base_url, service.llm_config.base_url)

    def test_minimal_client_wrapper_returns_answer(self) -> None:
        captured = {}

        def fake_request(method, path, payload, timeout):
            captured["method"] = method
            captured["path"] = path
            captured["payload"] = payload
            captured["timeout"] = timeout
            return {"answer": "这是测试答案。"}

        client = SPLClient(
            api_base="http://127.0.0.1:8000",
            llm={"base_url": "https://api.rcouyi.com/v1", "api_key": "k", "model": "gpt-5"},
            request_func=fake_request,
        )
        answer = client.ask_code_project(
            target="https://github.com/example/repo",
            question="这个项目做什么？",
            use_llm_for_build=False,
        )
        self.assertEqual(answer, "这是测试答案。")
        self.assertEqual(captured["method"], "POST")
        self.assertEqual(captured["path"], "/query")
        self.assertEqual(captured["payload"]["target"], "https://github.com/example/repo")
        self.assertEqual(captured["payload"]["question"], "这个项目做什么？")
        self.assertEqual(captured["payload"]["llm"]["model"], "gpt-5")

    def test_module_level_ask_code_project_wrapper(self) -> None:
        with patch("spl_system.client.SPLClient.ask_code_project", return_value="模块包装成功。") as mocked:
            answer = ask_code_project(
                target="./demo_projects/local_order_demo",
                question="整体功能是什么？",
                api_base="http://127.0.0.1:8000",
                llm={"base_url": "https://api.rcouyi.com/v1", "api_key": "k", "model": "gpt-5"},
                use_llm_for_build=False,
            )
        self.assertEqual(answer, "模块包装成功。")
        mocked.assert_called_once()

    def test_api_docs_and_openapi_are_available(self) -> None:
        app = create_app(self.base_dir / "settings.yaml")
        client = TestClient(app)

        health = client.get("/health")
        self.assertEqual(health.status_code, 200)
        self.assertEqual(health.json()["docs_url"], "/docs")

        openapi = client.get("/openapi.json")
        self.assertEqual(openapi.status_code, 200)
        paths = openapi.json()["paths"]
        self.assertIn("/query", paths)
        self.assertIn("/build", paths)


if __name__ == "__main__":
    unittest.main()
