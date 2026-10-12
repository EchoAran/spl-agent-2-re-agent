from __future__ import annotations

from data_store import (
    attach_order_status,
    create_order_record,
    deduct_stock,
    find_order,
    get_available_quantity,
    list_orders,
    normalize_quantity,
    normalize_sku,
    release_product,
    require_product,
    reserve_product,
    serialize_money,
)


def normalize_customer_id(customer_id: str) -> str:
    return str(customer_id or "").strip().lower()


def normalize_order_line(raw_line: dict) -> dict:
    return {
        "sku": normalize_sku(raw_line.get("sku")),
        "quantity": normalize_quantity(raw_line.get("quantity", 0)),
    }


def normalize_order_request(payload: dict) -> dict:
    return {
        "customer_id": normalize_customer_id(payload.get("customer_id")),
        "lines": [normalize_order_line(line) for line in payload.get("lines", [])],
    }


def validate_customer(customer_id: str) -> None:
    if not customer_id:
        raise ValueError("customer_id is required")


def validate_lines(lines: list[dict]) -> None:
    if not lines:
        raise ValueError("At least one order line is required")
    for line in lines:
        if not line["sku"]:
            raise ValueError("Each order line requires a sku")
        if line["quantity"] <= 0:
            raise ValueError("Each order line requires a positive quantity")


def load_products_for_lines(lines: list[dict]) -> dict[str, dict]:
    products = {}
    for line in lines:
        products[line["sku"]] = require_product(line["sku"])
    return products


def ensure_quantity_available(lines: list[dict], products: dict[str, dict]) -> None:
    for line in lines:
        product = products[line["sku"]]
        available = get_available_quantity(product)
        if available < line["quantity"]:
            raise ValueError(f"Insufficient stock for {line['sku']}")


def calculate_line_subtotal(line: dict, product: dict) -> float:
    return round(float(product["price"]) * int(line["quantity"]), 2)


def build_order_lines(lines: list[dict], products: dict[str, dict]) -> list[dict]:
    order_lines = []
    for line in lines:
        product = products[line["sku"]]
        order_lines.append(
            {
                "sku": product["sku"],
                "product_name": product["name"],
                "unit_price": float(product["price"]),
                "quantity": int(line["quantity"]),
                "subtotal": calculate_line_subtotal(line, product),
            }
        )
    return order_lines


def calculate_order_total(order_lines: list[dict]) -> float:
    total = 0.0
    for line in order_lines:
        total += float(line["subtotal"])
    return round(total, 2)


def reserve_inventory(order_lines: list[dict]) -> list[dict]:
    reservations = []
    for line in order_lines:
        reservations.append(reserve_product(line["sku"], line["quantity"]))
    return reservations


def finalize_order(customer_id: str, order_lines: list[dict], total_amount: float) -> dict:
    order = create_order_record(customer_id, order_lines, total_amount)
    for line in order_lines:
        deduct_stock(line["sku"], line["quantity"])
        release_product(line["sku"], line["quantity"])
    return attach_order_status(find_order(order["order_id"]), "confirmed")


def build_receipt(order_record: dict) -> dict:
    return {
        "order_id": order_record["order_id"],
        "customer_id": order_record["customer_id"],
        "status": order_record["status"],
        "total_amount": serialize_money(order_record["total_amount"]),
        "line_count": len(order_record["lines"]),
    }


def submit_order(payload: dict) -> dict:
    request = normalize_order_request(payload)
    validate_customer(request["customer_id"])
    validate_lines(request["lines"])
    products = load_products_for_lines(request["lines"])
    ensure_quantity_available(request["lines"], products)
    order_lines = build_order_lines(request["lines"], products)
    reserve_inventory(order_lines)
    order_record = finalize_order(request["customer_id"], order_lines, calculate_order_total(order_lines))
    return build_receipt(order_record)


def load_order_details(order_id: str) -> dict:
    order = find_order(order_id)
    if order is None:
        raise ValueError(f"Unknown order: {order_id}")
    return build_receipt(order)


def cancel_order(order_id: str) -> dict:
    order = find_order(order_id)
    if order is None:
        raise ValueError(f"Unknown order: {order_id}")
    return attach_order_status(order, "cancelled")


def list_order_summaries() -> list[dict]:
    return [build_receipt(order) for order in list_orders()]

