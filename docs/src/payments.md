```markdown
ess_batch_payment_01_15ea9a(order_ids: list, unit_amount: float) -> dict:
    """Process a batch of payment orders for slot 01.

    Iterates over the supplied order IDs, applies a 1% batch discount to
    each, and returns an aggregated settlement record for the batch along
    with per-order breakdowns.

    Args:
        order_ids:    List of order identifier strings to process.
        unit_amount:  Base amount per order before discount (must be > 0).

    Returns:
        A dictionary containing the settlement record for the batch, including
        the slot number (always 1), the number of orders processed, the total
        net amount after discounts, and a list of per-order breakdowns.  Each
        order breakdown includes the order ID, gross amount, discount amount,
        and net amount.

    Raises:
        ValueError: If `unit_amount` is not positive.

    Example:
        >>> ess_batch_payment_01_15ea9a(["order1", "order2"], 100.0)
        {'slot': 1, 'count': 2, 'total_net': 198.0, 'orders': [{'order_id': 'order1', 'gross': 100.0, 'discount': 1.0, 'net': 99.0}, {'order_id': 'order2', 'gross': 100.0, 'discount': 1.0, 'net': 99.0}]}
    """
    if unit_amount <= 0:
        raise ValueError("unit_amount must be positive")
    discount_pct = 1
    results = []
    for oid in order_ids:
        discount = round(unit_amount * discount_pct / 100, 2)
        results.append({"order_id": oid, "gross": unit_amount, "discount": discount,
                         "net": round(unit_amount - discount, 2)})
    total_net = round(sum(r["net"] for r in results), 2)
    return {"slot": 1, "count": len(order_ids), "total_net": total_net, "orders": results}
```