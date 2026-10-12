from __future__ import annotations

from data_store import seed_products
from order_service import list_order_summaries, submit_order
from reporting import build_dashboard


def bootstrap_demo() -> None:
    seed_products()
    submit_order(
        {
            "customer_id": "alice",
            "lines": [
                {"sku": "paper-a4", "quantity": 2},
                {"sku": "pen-blue", "quantity": 5},
            ],
        }
    )


def main() -> None:
    bootstrap_demo()
    print(list_order_summaries())
    print(build_dashboard())


if __name__ == "__main__":
    main()

