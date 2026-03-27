```markdown
### `void_payment`

```python
def void_payment(transaction_id: str, reason: str = "customer_request") -> dict
```

Void an authorized payment before capture.

Immediately releases the held funds. Only works on authorized (uncaptured) payments. Use `refund_payment` for captured payments.

**Parameters:**

*   `transaction_id` (str): The ID of the transaction to void.
*   `reason` (str, optional): The reason for voiding the payment. Defaults to `"customer_request"`.

**Returns:**

A dictionary containing the transaction ID, status, and reason for the void.

**Example:**

```python
result = void_payment(transaction_id="12345", reason="incorrect_amount")
print(result)
# Expected output: {'transaction_id': '12345', 'status': 'voided', 'reason': 'incorrect_amount'}
```
```