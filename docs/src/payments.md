```markdown
### New Function: `issue_refund_9ee8b6`

#### Description
Issue a refund for a completed order. This function generates a refund record with a unique transaction ID. It includes a basic validation to ensure the refund amount is positive.

#### Parameters
*   `order_id` (`str`): Identifier of the order to refund.
*   `amount` (`float`): Refund amount (must be > 0).
*   `reason` (`str`): Human-readable reason for the refund (for audit trail).

#### Returns
*   `dict`: A dictionary containing the refund details with the following keys:
    *   `refund_id` (`str`): A unique identifier for the refund transaction.
    *   `order_id` (`str`): The identifier of the order being refunded.
    *   `amount` (`float`): The amount refunded.
    *   `reason` (`str`): The reason provided for the refund.
    *   `status` (`str`): The status of the refund, which is always "refunded".

#### Raises
*   `ValueError`: If the `amount` is not positive.

#### Example
```python
refund_details = issue_refund_9ee8b6(
    order_id="ORD12345",
    amount=50.00,
    reason="Customer returned item"
)
print(refund_details)
# Expected output (refund_id will be a unique UUID):
# {'refund_id': '...', 'order_id': 'ORD12345', 'amount': 50.0, 'reason': 'Customer returned item', 'status': 'refunded'}
```
```