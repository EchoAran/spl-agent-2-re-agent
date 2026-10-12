def checkout(user: dict, cart: list[dict], coupon: str | None = None) -> dict:
    """
    Create an order: compute final total and charge the user's balance.
    Returns an order summary dict.
    """
    total = calc_total(cart, coupon)

    if total <= 0:
        raise ValueError("Total must be positive")

    if user.get("balance", 0) < total:
        return {
            "ok": False,
            "reason": "insufficient_funds",
            "need": total,
            "balance": user.get("balance", 0),
        }

    user["balance"] -= total
    return {"ok": True, "charged": total, "balance": user["balance"]}


def apply_discount(subtotal: int, coupon: str | None) -> int:
    """
    Apply a coupon to subtotal and return the discounted amount (integer cents).
    """
    if not coupon:
        return subtotal

    coupon = coupon.strip().upper()
    if coupon == "SAVE10":
        # 10% off
        return int(subtotal * 0.9)
    if coupon == "MINUS500":
        # 500 cents off, but not below 0
        return max(0, subtotal - 500)

    # unknown coupon: no discount
    return subtotal


def calc_total(cart: list[dict], coupon: str | None) -> int:
    """
    Sum items (price_cents * qty), then apply discount.
    Returns integer cents.
    """
    subtotal = 0
    for item in cart:
        price = int(item.get("price_cents", 0))
        qty = int(item.get("qty", 1))
        subtotal += price * qty

    return apply_discount(subtotal, coupon)
