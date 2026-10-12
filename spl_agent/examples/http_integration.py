from __future__ import annotations

import json
import urllib.request


API_BASE = "http://127.0.0.1:8000"


def post_json(path: str, payload: dict) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url=f"{API_BASE}{path}",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    result = post_json(
        "/query",
        {
            "target": "./demo_projects/local_order_demo",
            "project_name": "local_order_demo",
            "question": "这个项目的整体功能是什么？用户提交一个订单后，库存和订单结果是怎么一步步生成的？中间涉及哪些关键函数？",
            "prefer_legacy_spl": False,
            "force_rebuild": False,
            "use_llm_for_build": False,
            "export_spl": True,
            "include_trace": False,
            "llm": {
                "base_url": "https://api.rcouyi.com/v1",
                "api_key": "YOUR_KEY",
                "model": "gpt-5",
            },
        },
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
