```markdown
### `get_payment_status`

```python
def get_payment_status(transaction_id: str) -> dict
```

Retrieve the current status of a payment transaction.

**Parameters:**

*   `transaction_id` (str): The unique identifier for the payment transaction.

**Returns:**

A dictionary containing the transaction ID, status, and settlement status. For example:

```json
{"transaction_id": "your_transaction_id", "status": "completed", "settled": True}
```
