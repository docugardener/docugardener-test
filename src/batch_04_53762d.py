"""Batch payment processor for slot 04 (e2e run 53762d)."""


def process_batch_payment_04_53762d(order_ids: list, unit_amount: float) -> dict:
    """Process a batch of payment orders for slot 04.

    Iterates over the supplied order IDs, applies a 4% batch discount to
    each, and returns an aggregated settlement record for the batch along
    with per-order breakdowns.

    Args:
        order_ids:    List of order identifier strings to process.
        unit_amount:  Base amount per order before discount (must be > 0).
    """
    if unit_amount <= 0:
        raise ValueError("unit_amount must be positive")
    discount_pct = 4
    results = []
    for oid in order_ids:
        discount = round(unit_amount * discount_pct / 100, 2)
        results.append({"order_id": oid, "gross": unit_amount, "discount": discount,
                         "net": round(unit_amount - discount, 2)})
    total_net = round(sum(r["net"] for r in results), 2)
    return {"slot": 4, "count": len(order_ids), "total_net": total_net, "orders": results}

