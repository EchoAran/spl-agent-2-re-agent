# SPL Code Understanding API

## Overview

This service builds and caches an SPL tree for a Python project, then answers natural-language questions by navigating that SPL tree through a JSON-based agent loop.

Runtime truth:

- `spl_tree.json` is the authoritative runtime artifact
- `.spl` files are exported for debugging and inspection

The easiest integration path is:

1. Call `POST /query`
2. Pass a Git URL or local path plus one question
3. Read `answer` from the response

If the host system is also Python and runs locally, an even simpler option is to use [client.py](client.py) and call `ask_code_project(target, question)`.

FastAPI also exposes live interactive docs:

- `GET /docs`
- `GET /openapi.json`

## Startup

Install:

```bash
pip install -e .
```

Run:

```bash
spl-api --host 127.0.0.1 --port 8000 --config settings.yaml
```

or:

```bash
uvicorn spl_system.api.app:app --host 127.0.0.1 --port 8000
```

## Authentication

The API itself does not require an auth header by default.

LLM credentials come from:

- the server config file
- the optional `llm` block in each request

Request-level `llm` overrides are useful when another system wants to choose the model or credentials dynamically.

## Endpoints

### `GET /health`

Purpose:

- liveness check
- returns doc entrypoints

Example response:

```json
{
  "ok": true,
  "docs_url": "/docs",
  "openapi_url": "/openapi.json"
}
```

### `POST /build`

Purpose:

- build or load an SPL tree
- useful when you want to ask multiple questions against the same project

Request example:

```json
{
  "target": "./demo_projects/local_order_demo",
  "project_name": "local_order_demo",
  "prefer_legacy_spl": false,
  "force_rebuild": false,
  "use_llm_for_build": false,
  "export_spl": true
}
```

Response example:

```json
{
  "project_id": "local:d3e2216ac8d0d9ff",
  "project_name": "local_order_demo",
  "cache_hit": true,
  "source_type": "local",
  "normalized_source": "C:\\\\path\\\\to\\\\local_order_demo",
  "commit": null,
  "requested_ref": null,
  "spl_tree_path": ".spl_cache/local/.../spl_tree.json"
}
```

### `POST /ask`

Purpose:

- ask a question about an already-built project

Request example:

```json
{
  "project_id": "local:d3e2216ac8d0d9ff",
  "question": "这个项目的整体功能是什么？",
  "include_trace": true
}
```

Response example:

```json
{
  "answer": "这是一个本地内存级的下单与库存演示项目。",
  "rounds": 4,
  "stopped_by_limit": false,
  "tool_trace": [
    {
      "round": 1,
      "tool_name": "get_project_overview",
      "arguments": {},
      "result": {
        "ok": true
      }
    }
  ]
}
```

### `POST /query`

Purpose:

- one-shot build-or-load plus question answering
- recommended default integration endpoint

Request example:

```json
{
  "target": "./demo_projects/local_order_demo",
  "project_name": "local_order_demo",
  "question": "这个项目的整体功能是什么？用户提交一个订单后，库存和订单结果是怎么一步步生成的？中间涉及哪些关键函数？",
  "prefer_legacy_spl": false,
  "force_rebuild": false,
  "use_llm_for_build": false,
  "export_spl": true,
  "include_trace": false,
  "llm": {
    "base_url": "https://api.rcouyi.com/v1",
    "api_key": "YOUR_KEY",
    "model": "gpt-5"
  }
}
```

Response example:

```json
{
  "answer": "local_order_demo 是一个本地内存级的下单与库存演示项目。",
  "project_id": "local:d3e2216ac8d0d9ff",
  "project_name": "local_order_demo",
  "source_type": "local",
  "normalized_source": "C:\\\\path\\\\to\\\\local_order_demo",
  "commit": null,
  "cache_hit": true
}
```

If `include_trace=true`, the response also includes:

- `rounds`
- `stopped_by_limit`
- `tool_trace`

### `GET /projects/{project_id}/tree`

Purpose:

- fetch the full SPL tree JSON
- intended for debugging or advanced integrations

### `GET /projects/{project_id}/node?path=...`

Purpose:

- fetch one node by SPL path

Example:

```text
/projects/local:d3e2216ac8d0d9ff/node?path=/modules/order_service.py/function::submit_order/summary
```

## Source Input Rules

You can pass either:

- a Git URL
- a local filesystem path

Recommended input field:

- `target`

Alternative explicit fields:

- `repo_url`
- `local_path`

For Git sources:

- if `commit` is omitted, the service resolves the actual commit
- cache is isolated by normalized URL + resolved commit

For local sources:

- cache is isolated by normalized local path

## Integration Patterns

### Pattern 1: One-shot query

Use `POST /query` when another project just needs the final answer.

### Pattern 2: Build once, ask many

Use `POST /build` first, then call `POST /ask` multiple times with the returned `project_id`.

This is better when:

- one project receives multiple different questions
- you want to avoid rebuilding the SPL tree

### Pattern 3: External inspection

Use:

- `GET /projects/{project_id}/tree`
- `GET /projects/{project_id}/node`

This is useful when a host application wants to build custom tooling around the SPL structure.

## Error Handling

The API uses standard HTTP error responses.

Typical cases:

- `400`: invalid request, unsupported source, LLM/protocol error
- `404`: project or node not found

The response body follows FastAPI defaults:

```json
{
  "detail": "error message"
}
```

## Recommended Client Behavior

- Prefer `POST /query` first
- Cache `project_id` if you plan to ask follow-up questions
- Only request `include_trace=true` when debugging
- Pass request-level `llm` overrides if the caller wants dynamic model routing
