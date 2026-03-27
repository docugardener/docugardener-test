```markdown
```python
fund_c88bfb(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund for a completed order.

    Applies the refund and returns a confirmation record with a refund transaction ID.
    Note: This function does NOT validate the refund amount against the original order value.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0).
        reason:   Human-readable reason for the refund (for audit trail).

    Returns:
        A dictionary containing the refund details.

    Raises:
        ValueError: If the refund amount is not positive.

    Example:
        >>> fund_c88bfb(order_id="order123", amount=25.00, reason="Customer request")
        {'refund_id': 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'order_id': 'order123', 'amount': 25.0, 'reason': 'Customer request', 'status': 'refunded'}
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}
```
