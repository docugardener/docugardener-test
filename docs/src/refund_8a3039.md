```markdown
### `issue_refund_8a3039` Function
```python
def issue_refund_8a3039(order_id: str, amount: float, reason: str) -> dict:
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
```

**Description:**

Issue a refund for a completed order. This function generates a refund record with a unique transaction ID. It includes a basic validation to ensure the refund amount is positive.

**Parameters:**

*   `order_id` (`str`): Identifier of the order to refund.
*   `amount` (`float`): Refund amount. Must be greater than 0.
*   `reason` (`str`): Human-readable reason for the refund, used for audit trails.

**Returns:**

*   `dict`: A dictionary containing the refund details, including:
    *   `refund_id` (`str`): A unique identifier for the refund transaction.
    *   `order_id` (`str`): The identifier of the order being refunded.
    *   `amount` (`float`): The specified refund amount.
    *   `reason` (`str`): The reason provided for the refund.
    *   `status` (`str`): The status of the refund, which is always "refunded".

**Raises:**

*   `ValueError`: If the `amount` provided is not positive.

**Example:**

```python
refund_details = issue_refund_8a3039(order_id="ORD7890", amount=50.00, reason="Item damaged in transit")
print(refund_details)
# Expected output (refund_id will be a unique UUID):
# {'refund_id': '...', 'order_id': 'ORD7890', 'amount': 50.0, 'reason': 'Item damaged in transit', 'status': 'refunded'}
```
```