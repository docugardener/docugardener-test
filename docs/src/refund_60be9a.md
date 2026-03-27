```markdown
```python
def issue_refund_60be9a(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund record for a completed order.

    Creates a refund record with the provided details.  Does not validate
    the refund amount against the original order or process any actual refund.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0).
        reason:   Human-readable reason for the refund (for audit trail).

    Returns:
        dict with refund_id, order_id, amount, reason, and status keys.
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}
```
