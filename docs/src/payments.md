```markdown
### `cancel_payment`

```python
def cancel_payment(transaction_id: str, reason: str = "customer_request", notify_customer: bool = True, idempotency_key: str | None = None) -> dict
```

Cancels a pending payment before it is captured.

Only payments in `'pending'` or `'authorized'` state can be cancelled. Captured payments must use `refund_payment` instead.

**Parameters:**

-   `transaction_id` (*str*): The ID of the transaction to cancel.
-   `reason` (*str*, defaults to `"customer_request"`): The reason for the cancellation.
-   `notify_customer` (*bool*, defaults to `True`): Whether to notify the customer about the cancellation.
-   `idempotency_key` (*str | None*, defaults to `None`):  An optional idempotency key to prevent accidental duplicate cancellations.

**Returns:**

A dictionary containing the transaction ID, cancellation status, reason, and customer notification status.

```python
result = cancel_payment(transaction_id="123", reason="incorrect_amount")
print(result)
# Expected output: {'transaction_id': '123', 'status': 'cancelled', 'reason': 'incorrect_amount', 'customer_notified': True}
```
```python
result = cancel_payment(transaction_id="456", notify_customer=False)
print(result)
# Expected output: {'transaction_id': '456', 'status': 'cancelled', 'reason': 'customer_request', 'customer_notified': False}
```
