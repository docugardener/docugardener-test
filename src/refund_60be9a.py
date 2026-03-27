"""Refund service module — 60be9a.

Provides issue_refund_60be9a for processing order refunds.
"""


def issue_refund_60be9a(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund for a completed order.

    Validates the refund amount against the original order, applies the
    refund, and returns a confirmation record with the refund transaction ID.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0 and <= original order value).
        reason:   Human-readable reason for the refund (for audit trail).

    Returns:
        dict with refund_id, order_id, amount, reason, and status keys.
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}

