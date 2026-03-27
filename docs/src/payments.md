```markdown
### `schedule_payment`

```python
def schedule_payment(amount: float, currency: str = "USD", scheduled_at: str | None = None) -> dict
```

Schedule a payment for future execution.

`scheduled_at` should be an ISO 8601 datetime string.
If omitted, the payment is scheduled for the next business day.

**Parameters:**

-   `amount` (float): The payment amount.
-   `currency` (str, optional): The currency code (e.g., "USD"). Defaults to "USD".
-   `scheduled_at` (str | None, optional): An ISO 8601 datetime string specifying when to schedule the payment. If `None`, the payment is scheduled for the next business day. Defaults to `None`.

**Returns:**

A dictionary containing the transaction details, including:

-   `transaction_id` (str): A dummy transaction ID ("txn_sched_new").
-   `status` (str): The status of the scheduled payment ("scheduled").
-   `amount` (float): The payment amount.
-   `currency` (str): The currency code.
-   `scheduled_at` (str | None): The scheduled datetime string, or `None` if not specified.

**Example:**

```python
result = schedule_payment(amount=100.00, currency="EUR", scheduled_at="2024-03-15T10:00:00Z")
print(result)
# Expected output:
# {
#     'transaction_id': 'txn_sched_new',
#     'status': 'scheduled',
#     'amount': 100.0,
#     'currency': 'EUR',
#     'scheduled_at': '2024-03-15T10:00:00Z'
# }
```
```python
result = schedule_payment(amount=50.00)
print(result)
# Expected output:
# {
#     'transaction_id': 'txn_sched_new',
#     'status': 'scheduled',
#     'amount': 50.0,
#     'currency': 'USD',
#     'scheduled_at': None
# }
```
