```markdown
### `issue_refund_ad2a35(order_id: str, amount: float, reason: str) -> dict`

Generates a refund record for a completed order. This function validates that the refund amount is positive and returns a dictionary representing a new refund transaction. It does not interact with any external systems or databases to process the refund.

**Parameters:**

*   `order_id` (`str`): The identifier of the order for which the refund record is being generated.
*   `amount` (`float`): The amount of the refund. This value must be greater than 0.
*   `reason` (`str`): A human-readable reason for the refund, intended for audit trails.

**Returns:**

*   `dict`: A dictionary containing the details of the generated refund record. It includes the following keys:
    *   `refund_id` (`str`): A unique identifier generated for this refund transaction.
    *   `order_id` (`str`): The identifier of the order associated with the refund.
    *   `amount` (`float`): The specified refund amount.
    *   `reason` (`str`): The reason provided for the refund.
    *   `status` (`str`): The status of the refund, which is always `"refunded"`.

**Raises:**

*   `ValueError`: If the `amount` provided is less than or equal to 0.

**Example:**

```python
try:
    refund_record = issue_refund_ad2a35(
        order_id="ORD-12345",
        amount=50.75,
        reason="Customer changed mind"
    )
    print(refund_record)
    # Expected output (refund_id will vary):
    # {
    #     'refund_id': 'a1b2c3d4-e5f6-7890-1234-567890abcdef',
    #     'order_id': 'ORD-12345',
    #     'amount': 50.75,
    #     'reason': 'Customer changed mind',
    #     'status': 'refunded'
    # }

    # Example of invalid amount
    issue_refund_ad2a35(
        order_id="ORD-67890",
        amount=0,
        reason="Invalid amount test"
    )
except ValueError as e:
    print(f"Error: {e}")
    # Expected output: Error: refund amount must be positive
```
```