from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable, Dict, Optional


RequestFunction = Callable[[str, str, Optional[Dict[str, Any]], int], Dict[str, Any]]


class APIError(RuntimeError):
    """Raised when the local SPL HTTP service returns an error response."""


class SPLClient:
    """
    Minimal local client for another system to call the SPL HTTP API.

    Typical use:

        client = SPLClient()
        answer = client.ask_code_project(
            target="https://github.com/kennethreitz/records",
            question="这个项目的整体功能是什么？",
        )
    """

    def __init__(
        self,
        api_base: str = "http://127.0.0.1:8000",
        timeout_sec: int = 300,
        llm: Optional[Dict[str, Any]] = None,
        request_func: Optional[RequestFunction] = None,
    ) -> None:
        self.api_base = api_base.rstrip("/")
        self.timeout_sec = timeout_sec
        self.default_llm = dict(llm or {})
        self._request_func = request_func

    def health(self) -> Dict[str, Any]:
        return self._request("GET", "/health", payload=None)

    def build(
        self,
        target: str,
        *,
        source_type: Optional[str] = None,
        repo_url: Optional[str] = None,
        commit: Optional[str] = None,
        local_path: Optional[str] = None,
        project_name: Optional[str] = None,
        prefer_legacy_spl: bool = True,
        force_rebuild: bool = False,
        use_llm_for_build: bool = True,
        export_spl: bool = True,
        llm: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "target": target,
            "source_type": source_type,
            "repo_url": repo_url,
            "commit": commit,
            "local_path": local_path,
            "project_name": project_name,
            "prefer_legacy_spl": prefer_legacy_spl,
            "force_rebuild": force_rebuild,
            "use_llm_for_build": use_llm_for_build,
            "export_spl": export_spl,
        }
        merged_llm = self._merged_llm(llm)
        if merged_llm:
            payload["llm"] = merged_llm
        return self._request("POST", "/build", payload=payload)

    def ask(
        self,
        project_id: str,
        question: str,
        *,
        include_trace: bool = False,
        llm: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "project_id": project_id,
            "question": question,
            "include_trace": include_trace,
        }
        merged_llm = self._merged_llm(llm)
        if merged_llm:
            payload["llm"] = merged_llm
        return self._request("POST", "/ask", payload=payload)

    def query(
        self,
        target: str,
        question: str,
        *,
        source_type: Optional[str] = None,
        repo_url: Optional[str] = None,
        commit: Optional[str] = None,
        local_path: Optional[str] = None,
        project_name: Optional[str] = None,
        prefer_legacy_spl: bool = True,
        force_rebuild: bool = False,
        use_llm_for_build: bool = True,
        export_spl: bool = True,
        include_trace: bool = False,
        llm: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "target": target,
            "question": question,
            "source_type": source_type,
            "repo_url": repo_url,
            "commit": commit,
            "local_path": local_path,
            "project_name": project_name,
            "prefer_legacy_spl": prefer_legacy_spl,
            "force_rebuild": force_rebuild,
            "use_llm_for_build": use_llm_for_build,
            "export_spl": export_spl,
            "include_trace": include_trace,
        }
        merged_llm = self._merged_llm(llm)
        if merged_llm:
            payload["llm"] = merged_llm
        return self._request("POST", "/query", payload=payload)

    def ask_code_project(
        self,
        target: str,
        question: str,
        *,
        source_type: Optional[str] = None,
        project_name: Optional[str] = None,
        llm: Optional[Dict[str, Any]] = None,
        use_llm_for_build: bool = True,
    ) -> str:
        """
        Smallest possible integration helper.

        Another local system usually only needs:

        - target
        - question

        Returns just the final answer string.
        """

        result = self.query(
            target=target,
            question=question,
            source_type=source_type,
            project_name=project_name,
            llm=llm,
            use_llm_for_build=use_llm_for_build,
        )
        return str(result["answer"])

    def _merged_llm(self, llm: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        merged = dict(self.default_llm)
        merged.update({key: value for key, value in (llm or {}).items() if value is not None})
        return merged

    def _request(self, method: str, path: str, payload: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if self._request_func is not None:
            return self._request_func(method, path, payload, self.timeout_sec)

        url = f"{self.api_base}{path}"
        if method == "GET":
            if payload:
                url = f"{url}?{urllib.parse.urlencode(payload)}"
            request = urllib.request.Request(url=url, method="GET")
        else:
            body = json.dumps(payload or {}, ensure_ascii=False).encode("utf-8")
            request = urllib.request.Request(
                url=url,
                data=body,
                headers={"Content-Type": "application/json"},
                method=method,
            )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout_sec) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise APIError(f"HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise APIError(f"Request failed: {exc}") from exc


def ask_code_project(
    target: str,
    question: str,
    *,
    api_base: str = "http://127.0.0.1:8000",
    timeout_sec: int = 300,
    llm: Optional[Dict[str, Any]] = None,
    source_type: Optional[str] = None,
    project_name: Optional[str] = None,
    use_llm_for_build: bool = True,
) -> str:
    """
    Minimal one-function wrapper for external systems.

    Example:

        answer = ask_code_project(
            target="https://github.com/kennethreitz/records",
            question="这个项目的整体功能是什么？",
            llm={
                "base_url": "https://api.rcouyi.com/v1",
                "api_key": "YOUR_KEY",
                "model": "gpt-5",
            },
        )
    """

    client = SPLClient(api_base=api_base, timeout_sec=timeout_sec, llm=llm)
    return client.ask_code_project(
        target=target,
        question=question,
        source_type=source_type,
        project_name=project_name,
        use_llm_for_build=use_llm_for_build,
    )
