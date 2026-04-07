from __future__ import annotations

import difflib
import re
from collections import deque
from typing import Any, Dict, List

from .models import SPLTree


class SPLToolset:
    def __init__(self, tree: SPLTree):
        self.tree = tree

    def inspect_children(self, path: str = "/") -> Dict[str, Any]:
        node = self.tree.get_node(path)
        if node is None:
            return {"ok": False, "error": f"Path not found: {path}"}
        return {
            "ok": True,
            "path": node.path,
            "node_type": node.node_type,
            "children": [
                {"name": child.name, "node_type": child.node_type, "path": child.path}
                for child in node.children
            ],
        }

    def get_project_overview(self) -> Dict[str, Any]:
        modules = []
        for node in self.tree.iter_nodes():
            if node.node_type != "module":
                continue
            functions_field = self.tree.get_node(f"{node.path}/functions")
            functions = functions_field.children if functions_field is not None else []
            modules.append(
                {
                    "module_path": node.name,
                    "function_count": len(functions),
                    "sample_functions": [
                        {
                            "qualified_name": str(func.metadata.get("qualified_name") or func.name),
                            "summary": self._field_content(func.path, "summary") or "",
                            "path": func.path,
                        }
                        for func in functions[:5]
                    ],
                }
            )
        return {
            "ok": True,
            "project_name": self.tree.project_name,
            "module_count": len(modules),
            "function_count": len(self.tree.function_nodes()),
            "modules": modules,
        }

    def get_node(self, path: str) -> Dict[str, Any]:
        node = self.tree.get_node(path)
        if node is None:
            return {"ok": False, "error": f"Path not found: {path}"}
        return {
            "ok": True,
            "node": {
                "node_type": node.node_type,
                "name": node.name,
                "path": node.path,
                "content": node.content,
                "metadata": node.metadata,
                "children_count": len(node.children),
            },
        }

    def get_calls(self, function_path: str) -> Dict[str, Any]:
        node = self.tree.get_node(function_path)
        if node is None:
            return {"ok": False, "error": f"Function path not found: {function_path}"}
        calls_node = self.tree.get_node(f"{function_path}/calls")
        if calls_node is None:
            return {"ok": False, "error": f"Calls field not found under: {function_path}"}
        return {"ok": True, "function_path": function_path, "calls": calls_node.content or []}

    def get_callers(self, function_path: str) -> Dict[str, Any]:
        node = self.tree.get_node(function_path)
        if node is None:
            return {"ok": False, "error": f"Function path not found: {function_path}"}
        callers_node = self.tree.get_node(f"{function_path}/called_by")
        if callers_node is None:
            return {"ok": False, "error": f"called_by field not found under: {function_path}"}
        return {"ok": True, "function_path": function_path, "callers": callers_node.content or []}

    def trace_call_graph(
        self,
        function_path: str,
        direction: str = "outbound",
        max_depth: int = 2,
        max_nodes: int = 20,
    ) -> Dict[str, Any]:
        root = self.tree.get_node(function_path)
        if root is None or root.node_type != "function":
            return {"ok": False, "error": f"Function path not found: {function_path}"}
        if direction not in {"outbound", "inbound"}:
            return {"ok": False, "error": "direction must be outbound or inbound"}

        relation_field = "calls" if direction == "outbound" else "called_by"
        queue = deque([(function_path, 0)])
        visited = {function_path}
        edges: List[Dict[str, Any]] = []
        nodes: Dict[str, Dict[str, Any]] = {
            function_path: self._compact_function(function_path),
        }

        while queue and len(nodes) < max_nodes:
            current_path, depth = queue.popleft()
            if depth >= max_depth:
                continue
            next_paths = self._field_content(current_path, relation_field) or []
            for next_path in next_paths:
                if next_path not in nodes:
                    nodes[next_path] = self._compact_function(next_path)
                edges.append(
                    {
                        "from": current_path if direction == "outbound" else next_path,
                        "to": next_path if direction == "outbound" else current_path,
                        "depth": depth + 1,
                    }
                )
                if next_path not in visited and len(nodes) < max_nodes:
                    visited.add(next_path)
                    queue.append((next_path, depth + 1))

        return {
            "ok": True,
            "function_path": function_path,
            "direction": direction,
            "max_depth": max_depth,
            "nodes": list(nodes.values()),
            "edges": edges,
        }

    def find_functions(self, query: str, module_path: str = "", limit: int = 8) -> Dict[str, Any]:
        query_text = (query or "").strip().lower()
        if not query_text:
            return {"ok": False, "error": "query must not be empty"}

        query_tokens = self._tokens(query_text)
        matches: List[Dict[str, Any]] = []
        for node in self.tree.function_nodes():
            node_module_path = str(node.metadata.get("module_path") or "")
            if module_path and node_module_path != module_path:
                continue

            qualified_name = str(node.metadata.get("qualified_name") or node.name)
            short_name = qualified_name.split(".")[-1]
            summary = self._field_content(node.path, "summary") or ""
            signature = str(node.metadata.get("signature") or "")
            analysis_context = self._field_content(node.path, "analysis_context") or {}

            score, reasons = self._score_function_candidate(
                query_text=query_text,
                query_tokens=query_tokens,
                qualified_name=qualified_name,
                short_name=short_name,
                module_path=node_module_path,
                summary=summary,
                signature=signature,
                analysis_context=analysis_context,
            )
            if score >= 0.4:
                matches.append(
                    {
                        "function_path": node.path,
                        "qualified_name": qualified_name,
                        "module_path": node_module_path,
                        "signature": signature,
                        "summary": summary,
                        "score": round(score, 4),
                        "match_reasons": reasons[:4],
                    }
                )

        matches.sort(key=lambda item: (-item["score"], item["qualified_name"]))
        return {"ok": True, "query": query, "matches": matches[: max(1, min(limit, 20))]}

    def get_function_overview(self, function_path: str) -> Dict[str, Any]:
        node = self.tree.get_node(function_path)
        if node is None:
            return {"ok": False, "error": f"Function path not found: {function_path}"}
        if node.node_type != "function":
            return {"ok": False, "error": f"Path is not a function node: {function_path}"}

        inputs = self._field_content(function_path, "inputs") or []
        outputs = self._field_content(function_path, "outputs") or []
        calls = self._field_content(function_path, "calls") or []
        callers = self._field_content(function_path, "called_by") or []
        summary = self._field_content(function_path, "summary") or ""
        available_fields = [child.name for child in node.children if child.node_type == "field" and child.name != "raw_spl"]
        return {
            "ok": True,
            "function": {
                "path": function_path,
                "qualified_name": str(node.metadata.get("qualified_name") or node.name),
                "module_path": str(node.metadata.get("module_path") or ""),
                "signature": str(node.metadata.get("signature") or ""),
                "summary": summary,
                "input_count": len(inputs),
                "output_count": len(outputs),
                "calls_count": len(calls),
                "callers_count": len(callers),
                "sub_analysis_count": int(node.metadata.get("sub_analysis_count") or 0),
                "dependency_count": int(node.metadata.get("dependency_count") or 0),
                "available_fields": available_fields,
            },
        }

    def get_function_field(self, function_path: str, field_name: str) -> Dict[str, Any]:
        node = self.tree.get_node(function_path)
        if node is None:
            return {"ok": False, "error": f"Function path not found: {function_path}"}
        field_path = f"{function_path}/{field_name}"
        field_node = self.tree.get_node(field_path)
        if field_node is None:
            return {"ok": False, "error": f"Field not found: {field_name}"}
        return {
            "ok": True,
            "function_path": function_path,
            "field_name": field_name,
            "field_path": field_node.path,
            "content": field_node.content,
        }

    def get_flow_steps(
        self,
        function_path: str,
        flow_name: str = "main_flow",
        flow_index: int = 1,
        start_step: int = 1,
        end_step: int = 5,
    ) -> Dict[str, Any]:
        field_node = self.tree.get_node(f"{function_path}/{flow_name}")
        if field_node is None:
            return {"ok": False, "error": f"Flow field not found: {flow_name}"}
        if start_step < 1 or end_step < start_step:
            return {"ok": False, "error": "Invalid step range"}

        if flow_name == "main_flow":
            items = field_node.children
            selected = items[start_step - 1:end_step]
            return {
                "ok": True,
                "function_path": function_path,
                "flow_name": flow_name,
                "steps": [child.content for child in selected],
                "range": {"start_step": start_step, "end_step": end_step},
                "total_steps": len(items),
            }

        flow_nodes = field_node.children
        if flow_index < 1 or flow_index > len(flow_nodes):
            return {"ok": False, "error": f"flow_index out of range for {flow_name}"}
        flow_node = flow_nodes[flow_index - 1]
        selected = flow_node.children[start_step - 1:end_step]
        return {
            "ok": True,
            "function_path": function_path,
            "flow_name": flow_name,
            "flow_index": flow_index,
            "flow_content": flow_node.content,
            "steps": [child.content for child in selected],
            "range": {"start_step": start_step, "end_step": end_step},
            "total_steps": len(flow_node.children),
        }

    def get_function_spl_fragment(
        self,
        function_path: str,
        include_fields: List[str],
        main_flow_start_step: int = 1,
        main_flow_end_step: int = 5,
    ) -> Dict[str, Any]:
        node = self.tree.get_node(function_path)
        if node is None:
            return {"ok": False, "error": f"Function path not found: {function_path}"}
        if node.node_type != "function":
            return {"ok": False, "error": f"Path is not a function node: {function_path}"}

        allowed_fields = {
            "summary",
            "inputs",
            "outputs",
            "main_flow",
            "alternative_flows",
            "exception_flows",
            "calls",
            "called_by",
            "analysis_context",
        }
        normalized_fields = [field for field in include_fields if field in allowed_fields]
        if not normalized_fields:
            return {"ok": False, "error": "include_fields must contain at least one supported field"}

        fragment: Dict[str, Any] = {
            "worker_name": str(node.metadata.get("qualified_name") or node.name),
            "module_path": str(node.metadata.get("module_path") or ""),
            "signature": str(node.metadata.get("signature") or ""),
            "fields": {},
        }

        for field_name in normalized_fields:
            if field_name == "main_flow":
                partial = self.get_flow_steps(
                    function_path=function_path,
                    flow_name="main_flow",
                    start_step=main_flow_start_step,
                    end_step=main_flow_end_step,
                )
                if partial.get("ok"):
                    fragment["fields"]["main_flow"] = {
                        "steps": partial["steps"],
                        "range": partial["range"],
                        "total_steps": partial["total_steps"],
                    }
            else:
                fragment["fields"][field_name] = self._field_content(function_path, field_name)

        return {"ok": True, "function_path": function_path, "fragment": fragment}

    def get_module_overview(self, module_path: str) -> Dict[str, Any]:
        target_module = None
        for node in self.tree.iter_nodes():
            if node.node_type == "module" and node.name == module_path:
                target_module = node
                break
        if target_module is None:
            return {"ok": False, "error": f"Module not found: {module_path}"}

        functions = []
        functions_field = self.tree.get_node(f"{target_module.path}/functions")
        if functions_field is not None:
            for function_node in functions_field.children:
                functions.append(
                    {
                        "path": function_node.path,
                        "qualified_name": str(function_node.metadata.get("qualified_name") or function_node.name),
                        "signature": str(function_node.metadata.get("signature") or ""),
                        "summary": self._field_content(function_node.path, "summary") or "",
                    }
                )
        return {
            "ok": True,
            "module_path": module_path,
            "function_count": len(functions),
            "functions": functions,
        }

    def _compact_function(self, function_path: str) -> Dict[str, Any]:
        node = self.tree.get_node(function_path)
        if node is None:
            return {"path": function_path, "missing": True}
        return {
            "path": function_path,
            "qualified_name": str(node.metadata.get("qualified_name") or node.name),
            "module_path": str(node.metadata.get("module_path") or ""),
            "summary": self._field_content(function_path, "summary") or "",
        }

    def _field_content(self, function_path: str, field_name: str) -> Any:
        field_node = self.tree.get_node(f"{function_path}/{field_name}")
        if field_node is None:
            return None
        return field_node.content

    def _score_function_candidate(
        self,
        query_text: str,
        query_tokens: List[str],
        qualified_name: str,
        short_name: str,
        module_path: str,
        summary: str,
        signature: str,
        analysis_context: Dict[str, Any],
    ) -> tuple[float, List[str]]:
        reasons: List[str] = []
        score = 0.0

        haystacks = [qualified_name.lower(), short_name.lower(), module_path.lower(), summary.lower(), signature.lower()]
        query_token_set = set(query_tokens)
        text_token_set = set(self._tokens(" ".join(haystacks)))
        overlap = len(query_token_set & text_token_set)
        if query_text == qualified_name.lower():
            score = 1.0
            reasons.append("exact qualified name match")
        elif query_text == short_name.lower():
            score = 0.99
            reasons.append("exact short name match")
        else:
            if query_text in qualified_name.lower():
                score += 0.45
                reasons.append("query appears in qualified name")
            if query_text in short_name.lower():
                score += 0.42
                reasons.append("query appears in short name")
            if query_text in module_path.lower():
                score += 0.25
                reasons.append("query appears in module path")
            if query_text in summary.lower():
                score += 0.3
                reasons.append("query appears in summary")
            if overlap:
                score += min(0.3, overlap / max(1, len(query_token_set)) * 0.3)
                reasons.append(f"{overlap} token overlap")
            best_ratio = max(difflib.SequenceMatcher(None, query_text, hay).ratio() for hay in haystacks if hay)
            score += best_ratio * 0.15
            if best_ratio >= 0.65:
                reasons.append("high fuzzy similarity")

        dependency_count = len((analysis_context or {}).get("dependency_context", []))
        if dependency_count:
            score += min(0.05, dependency_count * 0.01)
            reasons.append("has dependency context")
        return min(score, 1.0), reasons

    def _tokens(self, text: str) -> List[str]:
        return [token for token in re.split(r"[^a-z0-9_]+", text.lower()) if token]

    @staticmethod
    def tool_definitions() -> List[Dict[str, Any]]:
        return [
            {
                "name": "get_project_overview",
                "description": "Return a lightweight overview of the whole project: modules, function counts, and a few sample function summaries.",
                "arguments_schema": {"type": "object", "properties": {}, "required": []},
            },
            {
                "name": "inspect_children",
                "description": "List the direct children of an SPL node without returning their full content. Use this for structure probing.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "SPL node path. Use '/' for the project root."}
                    },
                    "required": ["path"],
                },
            },
            {
                "name": "find_functions",
                "description": "Locate likely function nodes by name, module, signature, summary, and analysis context. Use this when you need to locate a function from a natural-language clue.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "module_path": {"type": "string"},
                        "limit": {"type": "integer", "default": 8},
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "get_module_overview",
                "description": "List the functions in one module with lightweight summaries. Use this before opening multiple functions in the same module.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {"module_path": {"type": "string"}},
                    "required": ["module_path"],
                },
            },
            {
                "name": "get_function_overview",
                "description": "Get a lightweight overview of a single function, including signature, summary, call counts, and available fields.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {"function_path": {"type": "string"}},
                    "required": ["function_path"],
                },
            },
            {
                "name": "trace_call_graph",
                "description": "Trace inbound or outbound call relationships from one function without opening full function bodies.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {
                        "function_path": {"type": "string"},
                        "direction": {"type": "string", "enum": ["outbound", "inbound"], "default": "outbound"},
                        "max_depth": {"type": "integer", "default": 2},
                        "max_nodes": {"type": "integer", "default": 20},
                    },
                    "required": ["function_path"],
                },
            },
            {
                "name": "get_function_field",
                "description": "Fetch exactly one function field such as summary, inputs, outputs, main_flow, calls, called_by, or analysis_context.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {
                        "function_path": {"type": "string"},
                        "field_name": {"type": "string"},
                    },
                    "required": ["function_path", "field_name"],
                },
            },
            {
                "name": "get_flow_steps",
                "description": "Fetch only a selected step range from a flow instead of retrieving the full flow.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {
                        "function_path": {"type": "string"},
                        "flow_name": {"type": "string", "default": "main_flow"},
                        "flow_index": {"type": "integer", "default": 1},
                        "start_step": {"type": "integer", "default": 1},
                        "end_step": {"type": "integer", "default": 5},
                    },
                    "required": ["function_path"],
                },
            },
            {
                "name": "get_function_spl_fragment",
                "description": "Return a JSON fragment corresponding to only selected parts of a function SPL.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {
                        "function_path": {"type": "string"},
                        "include_fields": {"type": "array", "items": {"type": "string"}},
                        "main_flow_start_step": {"type": "integer", "default": 1},
                        "main_flow_end_step": {"type": "integer", "default": 5},
                    },
                    "required": ["function_path", "include_fields"],
                },
            },
            {
                "name": "get_calls",
                "description": "Return the list of functions called by the given function node.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {"function_path": {"type": "string"}},
                    "required": ["function_path"],
                },
            },
            {
                "name": "get_callers",
                "description": "Return the list of functions that call the given function node.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {"function_path": {"type": "string"}},
                    "required": ["function_path"],
                },
            },
            {
                "name": "get_node",
                "description": "Get the full content and metadata of a specific SPL node by path. Use only when lighter tools are insufficient.",
                "arguments_schema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"],
                },
            },
        ]
