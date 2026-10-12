from __future__ import annotations

from collections import defaultdict

from data_store import list_orders, serialize_money
from order_service import load_order_details


def fetch_order_rows() -> list[dict]:
    rows = []
    for order in list_orders():
        for line in order["lines"]:
            rows.append(
                {
                    "order_id": order["order_id"],
                    "customer_id": order["customer_id"],
                    "status": order["status"],
                    "sku": line["sku"],
                    "quantity": line["quantity"],
                    "subtotal": line["subtotal"],
                }
            )
    return rows


def group_rows_by_order(rows: list[dict]) -> dict[str, list[dict]]:
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["order_id"]].append(row)
    return dict(grouped)


def count_orders(rows: list[dict]) -> int:
    return len({row["order_id"] for row in rows})


def sum_revenue(rows: list[dict]) -> float:
    total = 0.0
    for row in rows:
        total += float(row["subtotal"])
    return round(total, 2)


def sum_quantity_by_sku(rows: list[dict]) -> dict[str, int]:
    totals = defaultdict(int)
    for row in rows:
        totals[row["sku"]] += int(row["quantity"])
    return dict(sorted(totals.items()))


def build_order_snapshot(rows: list[dict]) -> list[dict]:
    snapshots = []
    for order_id, order_rows in group_rows_by_order(rows).items():
        snapshots.append(
            {
                "order_id": order_id,
                "customer_id": order_rows[0]["customer_id"],
                "status": order_rows[0]["status"],
                "line_count": len(order_rows),
                "total_amount": serialize_money(sum_revenue(order_rows)),
            }
        )
    return snapshots


def build_dashboard() -> dict:
    rows = fetch_order_rows()
    return {
        "order_count": count_orders(rows),
        "revenue": serialize_money(sum_revenue(rows)),
        "sku_demand": sum_quantity_by_sku(rows),
        "recent_orders": build_order_snapshot(rows),
    }


def build_recent_order_report(limit: int = 5) -> list[dict]:
    snapshots = build_order_snapshot(fetch_order_rows())
    return snapshots[-limit:]


def export_dashboard_text() -> str:
    dashboard = build_dashboard()
    lines = [
        f"order_count={dashboard['order_count']}",
        f"revenue={dashboard['revenue']}",
        f"sku_demand={dashboard['sku_demand']}",
    ]
    return "\n".join(lines)


def trace_order_flow(order_id: str) -> dict:
    order = load_order_details(order_id)
    return {
        "order": order,
        "dashboard": build_dashboard(),
    }

