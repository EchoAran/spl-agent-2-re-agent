# SPL Code Understanding API

This project is organized around `spl_tree.json` as the runtime source of truth.

## What it does

- Builds an SPL semantic tree for a Python project from either a Git URL or a local path
- Persists the runtime tree as `spl_tree.json`
- Exports `.spl` files as debugging artifacts
- Answers questions by navigating the SPL tree through a JSON-based agent loop
- Exposes a FastAPI HTTP service for direct integration into other projects

## Quick start

Install:

```bash
pip install -e .
```

Run the HTTP service:

```bash
spl-api --host 127.0.0.1 --port 8000 --config settings.yaml
```

Open:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/openapi.json`

## Simplest integration endpoint

Use `POST /query`.

Example request body:

```json
{
  "target": "./demo_projects/local_order_demo",
  "project_name": "local_order_demo",
  "question": "这个项目的整体功能是什么？用户提交一个订单后，库存和订单结果是怎么一步步生成的？中间涉及哪些关键函数？",
  "prefer_legacy_spl": false,
  "force_rebuild": false,
  "use_llm_for_build": false,
  "export_spl": true,
  "llm": {
    "base_url": "https://api.rcouyi.com/v1",
    "api_key": "YOUR_KEY",
    "model": "gpt-5"
  }
}
```

## Main entrypoints

- `spl-run`
- `spl-api`
- `spl-toolkit`

## Documentation

- API reference: [API.md](API.md)
- Minimal local client: [client.py](client.py)
- Minimal HTTP client example: [examples/http_integration.py](examples/http_integration.py)

## Simplest local integration

If another local Python system only wants:

- one project URL or local path
- one question

it can directly use [client.py](client.py):

```python
from client import ask_code_project

answer = ask_code_project(
    target="https://github.com/kennethreitz/records",
    question="这个项目的整体功能是什么？",
    llm={
        "base_url": "https://api.rcouyi.com/v1",
        "api_key": "YOUR_KEY",
        "model": "gpt-5"
    }
)

print(answer)
```

## Local batch mode

```bash
python run_from_config.py --config settings.yaml
```

## Tests

```bash
python -m unittest discover -s tests -v
```
