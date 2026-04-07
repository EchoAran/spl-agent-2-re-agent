from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from spl_system.core.config import AppConfig, LLMConfig
from spl_system.core.service import SPLProjectService


class LLMOverrideRequest(BaseModel):
    api_key: Optional[str] = Field(default=None, description="Optional API key override for this request.")
    base_url: Optional[str] = Field(default=None, description="Optional base URL override for this request.")
    model: Optional[str] = Field(default=None, description="Optional model override for this request.")
    temperature: Optional[float] = Field(default=None, ge=0.0, le=2.0, description="Optional temperature override.")
    timeout_sec: Optional[int] = Field(default=None, ge=5, description="Optional timeout override in seconds.")


class BuildRequest(BaseModel):
    source_type: Optional[str] = Field(default=None, pattern="^(git|local)$", description="Explicit source type. If omitted, inferred from target.")
    target: Optional[str] = Field(default=None, description="Git URL or local path. Preferred single source field.")
    repo_url: Optional[str] = Field(default=None, description="Git repository URL. Optional alternative to target.")
    commit: Optional[str] = Field(default=None, description="Optional git revision. If omitted for git sources, the service resolves the actual commit.")
    local_path: Optional[str] = Field(default=None, description="Local project path. Optional alternative to target.")
    project_name: Optional[str] = Field(default=None, description="Optional display name override.")
    prefer_legacy_spl: bool = Field(default=True, description="If true, reuse legacy Result/*.spl when available.")
    force_rebuild: bool = Field(default=False, description="If true, ignore cache and rebuild.")
    use_llm_for_build: bool = Field(default=True, description="If true, use the LLM during SPL construction.")
    export_spl: bool = Field(default=True, description="If true, export .spl files alongside spl_tree.json.")
    llm: Optional[LLMOverrideRequest] = Field(default=None, description="Optional request-level LLM override.")


class AskRequest(BaseModel):
    project_id: str = Field(description="Project identifier returned by /build or /query.")
    question: str = Field(description="Natural-language question about the built project.")
    include_trace: bool = Field(default=False, description="If true, include agent tool trace in the response.")
    llm: Optional[LLMOverrideRequest] = Field(default=None, description="Optional request-level LLM override.")


class QueryRequest(BaseModel):
    question: str = Field(description="Natural-language question about the target project.")
    source_type: Optional[str] = Field(default=None, pattern="^(git|local)$", description="Explicit source type. If omitted, inferred from target.")
    target: Optional[str] = Field(default=None, description="Git URL or local path. Preferred single source field.")
    repo_url: Optional[str] = Field(default=None, description="Git repository URL. Optional alternative to target.")
    commit: Optional[str] = Field(default=None, description="Optional git revision. If omitted for git sources, the service resolves the actual commit.")
    local_path: Optional[str] = Field(default=None, description="Local project path. Optional alternative to target.")
    project_name: Optional[str] = Field(default=None, description="Optional display name override.")
    prefer_legacy_spl: bool = Field(default=True, description="If true, reuse legacy Result/*.spl when available.")
    force_rebuild: bool = Field(default=False, description="If true, ignore cache and rebuild.")
    use_llm_for_build: bool = Field(default=True, description="If true, use the LLM during SPL construction.")
    export_spl: bool = Field(default=True, description="If true, export .spl files alongside spl_tree.json.")
    include_trace: bool = Field(default=False, description="If true, include agent tool trace in the response.")
    llm: Optional[LLMOverrideRequest] = Field(default=None, description="Optional request-level LLM override.")


class HealthResponse(BaseModel):
    ok: bool
    docs_url: str
    openapi_url: str


class BuildResponse(BaseModel):
    project_id: str
    project_name: str
    cache_hit: bool
    source_type: str
    normalized_source: str
    commit: Optional[str] = None
    requested_ref: Optional[str] = None
    spl_tree_path: str


class ToolTraceItem(BaseModel):
    round: int
    tool_name: str
    arguments: Dict[str, Any]
    result: Dict[str, Any]


class AskResponse(BaseModel):
    answer: str
    rounds: Optional[int] = None
    stopped_by_limit: Optional[bool] = None
    tool_trace: Optional[List[ToolTraceItem]] = None


class QueryResponse(BaseModel):
    answer: str
    project_id: str
    project_name: str
    source_type: str
    normalized_source: str
    commit: Optional[str] = None
    cache_hit: bool
    rounds: Optional[int] = None
    stopped_by_limit: Optional[bool] = None
    tool_trace: Optional[List[ToolTraceItem]] = None


def create_app(config_path: str | Path = "settings.yaml") -> FastAPI:
    config_file = Path(config_path)
    if config_file.exists():
        config = AppConfig.load(config_file)
    else:
        config = AppConfig.model_validate(
            {
                "llm": {},
                "source": {"type": "local", "local_path": "."},
                "runtime": {},
                "question": "",
            }
        )

    base_dir = Path(__file__).resolve().parents[2]
    default_service = SPLProjectService.from_config(config, base_dir=base_dir)

    app = FastAPI(
        title="SPL Code Understanding API",
        version="1.1.0",
        summary="SPL-centered conversational code understanding for Python projects.",
        description=(
            "Builds and caches SPL trees for Python projects, then answers questions by navigating the SPL tree "
            "through a JSON-based agent loop. You can inspect the live schema at /openapi.json and try requests at /docs."
        ),
    )
    app.state.base_config = config
    app.state.base_dir = base_dir
    app.state.service = default_service

    def service_for_override(llm_override: Optional[LLMOverrideRequest]) -> SPLProjectService:
        if llm_override is None:
            return app.state.service
        merged_llm = app.state.base_config.llm.model_copy(
            update={key: value for key, value in llm_override.model_dump().items() if value is not None}
        )
        return SPLProjectService(
            base_dir=app.state.base_dir,
            llm_config=merged_llm,
            cache_dir=app.state.base_config.runtime.cache_dir,
            max_rounds=app.state.base_config.runtime.max_rounds,
            build_workers=app.state.base_config.runtime.build_workers,
        )

    @app.get(
        "/health",
        response_model=HealthResponse,
        tags=["system"],
        summary="Health check",
        description="Basic liveness probe plus the documentation endpoints exposed by FastAPI.",
    )
    def health() -> HealthResponse:
        return HealthResponse(ok=True, docs_url="/docs", openapi_url="/openapi.json")

    @app.post(
        "/build",
        response_model=BuildResponse,
        tags=["build"],
        summary="Build or load an SPL tree",
        description="Build an SPL tree from a Git URL or local path, or load it from cache if it already exists.",
    )
    def build(request: BuildRequest) -> BuildResponse:
        service = service_for_override(request.llm)
        try:
            result = service.build_project(
                source_type=request.source_type,
                target=request.target,
                repo_url=request.repo_url,
                commit=request.commit,
                local_path=request.local_path,
                project_name=request.project_name,
                prefer_legacy_spl=request.prefer_legacy_spl,
                force_rebuild=request.force_rebuild,
                use_llm_for_build=request.use_llm_for_build,
                export_spl=request.export_spl,
            )
            return BuildResponse(**result)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    @app.post(
        "/query",
        response_model=QueryResponse,
        tags=["qa"],
        summary="Build or reuse a project and answer a question",
        description="The simplest integration endpoint. Accepts a source plus a question, then returns the final answer and build metadata.",
    )
    def query(request: QueryRequest) -> QueryResponse:
        service = service_for_override(request.llm)
        try:
            result = service.query(
                question=request.question,
                source_type=request.source_type,
                target=request.target,
                repo_url=request.repo_url,
                commit=request.commit,
                local_path=request.local_path,
                project_name=request.project_name,
                prefer_legacy_spl=request.prefer_legacy_spl,
                force_rebuild=request.force_rebuild,
                use_llm_for_build=request.use_llm_for_build,
                export_spl=request.export_spl,
            )
            payload: Dict[str, Any] = {
                "answer": result["answer"],
                "project_id": result["project_id"],
                "project_name": result["project_name"],
                "source_type": result["source_type"],
                "normalized_source": result["normalized_source"],
                "commit": result["commit"],
                "cache_hit": result["cache_hit"],
            }
            if request.include_trace:
                payload["rounds"] = result["rounds"]
                payload["stopped_by_limit"] = result["stopped_by_limit"]
                payload["tool_trace"] = result["tool_trace"]
            return QueryResponse(**payload)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    @app.post(
        "/ask",
        response_model=AskResponse,
        tags=["qa"],
        summary="Ask a question about an already-built project",
        description="Use this after /build when you want to reuse the same project cache across multiple questions.",
    )
    def ask(request: AskRequest) -> AskResponse:
        service = service_for_override(request.llm)
        try:
            result = service.ask(request.project_id, request.question)
            payload: Dict[str, Any] = {"answer": result.answer}
            if request.include_trace:
                payload["rounds"] = result.rounds
                payload["stopped_by_limit"] = result.stopped_by_limit
                payload["tool_trace"] = [
                    {
                        "round": trace.round_index,
                        "tool_name": trace.tool_name,
                        "arguments": trace.arguments,
                        "result": trace.result,
                    }
                    for trace in result.traces
                ]
            return AskResponse(**payload)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    @app.get(
        "/projects/{project_id}/tree",
        tags=["inspection"],
        summary="Get the full SPL tree",
        description="Return the complete persisted SPL tree as JSON. This is mainly intended for debugging or advanced integration.",
    )
    def get_tree(project_id: str) -> dict[str, Any]:
        try:
            tree = app.state.service.get_tree(project_id)
            return tree.to_dict()
        except Exception as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get(
        "/projects/{project_id}/node",
        tags=["inspection"],
        summary="Get one SPL node by path",
        description="Fetch one SPL node by its absolute path inside the SPL tree.",
    )
    def get_node(
        project_id: str,
        path: str = Query(..., description="Absolute SPL node path such as /modules/test.py/function::checkout/summary"),
    ) -> dict[str, Any]:
        try:
            tree = app.state.service.get_tree(project_id)
            node = tree.get_node(path)
            if node is None:
                raise HTTPException(status_code=404, detail=f"Path not found: {path}")
            return node.to_dict()
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    return app


app = create_app()
