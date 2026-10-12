from __future__ import annotations

from copy import deepcopy
from datetime import datetime


PRODUCTS = []
ORDERS = []
RESERVATIONS = []


def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def normalize_sku(sku: str) -> str:
    return str(sku or "").strip().upper()


def normalize_quantity(quantity: int) -> int:
    return int(quantity or 0)


def reset_store() -> None:
    PRODUCTS.clear()
    ORDERS.clear()
    RESERVATIONS.clear()


def seed_products() -> list[dict]:
    reset_store()
    PRODUCTS.extend(
        [
            {"sku": "PAPER-A4", "name": "A4 Paper", "price": 24.0, "stock": 120},
            {"sku": "PEN-BLUE", "name": "Blue Pen", "price": 3.5, "stock": 260},
            {"sku": "NOTE-SMALL", "name": "Small Notebook", "price": 8.0, "stock": 90},
        ]
    )
    return list_products()


def list_products() -> list[dict]:
    return [clone_product(product) for product in PRODUCTS]


def clone_product(product: dict) -> dict:
    return deepcopy(product)


def find_product_by_sku(sku: str) -> dict | None:
    normalized = normalize_sku(sku)
    for product in PRODUCTS:
        if product["sku"] == normalized:
            return product
    return None


def require_product(sku: str) -> dict:
    product = find_product_by_sku(sku)
    if product is None:
        raise ValueError(f"Unknown SKU: {sku}")
    return product


def get_available_quantity(product: dict) -> int:
    reserved = sum_reserved_for_sku(product["sku"])
    return max(0, int(product["stock"]) - reserved)


def sum_reserved_for_sku(sku: str) -> int:
    normalized = normalize_sku(sku)
    total = 0
    for row in RESERVATIONS:
        if row["sku"] == normalized:
            total += int(row["quantity"])
    return total


def reserve_product(sku: str, quantity: int) -> dict:
    product = require_product(sku)
    quantity = normalize_quantity(quantity)
    available = get_available_quantity(product)
    if quantity <= 0:
        raise ValueError("Reservation quantity must be positive")
    if available < quantity:
        raise ValueError(f"Insufficient stock for {sku}")

    reservation = {
        "reservation_id": f"res-{len(RESERVATIONS) + 1}",
        "sku": product["sku"],
        "quantity": quantity,
        "created_at": now_iso(),
    }
    RESERVATIONS.append(reservation)
    return dict(reservation)


def release_product(sku: str, quantity: int) -> None:
    normalized = normalize_sku(sku)
    quantity = normalize_quantity(quantity)
    remaining = quantity
    for reservation in reversed(RESERVATIONS):
        if reservation["sku"] != normalized or remaining <= 0:
            continue
        used = min(remaining, reservation["quantity"])
        reservation["quantity"] -= used
        remaining -= used
    RESERVATIONS[:] = [row for row in RESERVATIONS if row["quantity"] > 0]


def deduct_stock(sku: str, quantity: int) -> None:
    product = require_product(sku)
    product["stock"] = int(product["stock"]) - normalize_quantity(quantity)


def create_order_record(customer_id: str, lines: list[dict], total_amount: float) -> dict:
    order = {
        "order_id": f"ord-{len(ORDERS) + 1}",
        "customer_id": customer_id,
        "status": "pending",
        "lines": deepcopy(lines),
        "total_amount": round(float(total_amount), 2),
        "created_at": now_iso(),
    }
    ORDERS.append(order)
    return deepcopy(order)


def attach_order_status(order: dict, status: str) -> dict:
    order["status"] = status
    return deepcopy(order)


def list_orders() -> list[dict]:
    return [deepcopy(order) for order in ORDERS]


def find_order(order_id: str) -> dict | None:
    for order in ORDERS:
        if order["order_id"] == order_id:
            return order
    return None


def list_reservations() -> list[dict]:
    return [dict(row) for row in RESERVATIONS]


def serialize_money(value: float) -> str:
    return f"{float(value):.2f}"

