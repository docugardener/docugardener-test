```markdown
### `issue_refund_8cd765` Function
```python
def issue_refund_8cd765(order_id: str, amount: float, reason: str) -> dict:
```

Issues a refund for a completed order. This function validates that the refund amount is positive, generates a unique refund ID, and returns a confirmation record.

**Parameters:**

*   `order_id` (`str`): Identifier of the order to refund.
*   `amount` (`float`): Refund amount (must be > 0).
*   `reason` (`str`): Human-readable reason for the refund (for audit trail).

**Returns:**

*   `dict`: A dictionary containing the refund details with the following keys:
    *   `refund_id` (`str`): A unique identifier for the refund transaction.
    *   `order_id` (`str`): The identifier of the order being refunded.
    *   `amount` (`float`): The amount refunded.
    *   `reason` (`str`): The reason provided for the refund.
    *   `status` (`str`): The status of the refund, which is always "refunded".

**Raises:**

*   `ValueError`: If the `amount` is not positive.

**Example:**

```python
refund_details = issue_refund_8cd765(order_id="ORD7890", amount=50.00, reason="Item damaged in transit")
print(refund_details)
# Expected output: {'refund_id': '...', 'order_id': 'ORD7890', 'amount': 50.00, 'reason': 'Item damaged in transit', 'status': 'refunded'}
```
```