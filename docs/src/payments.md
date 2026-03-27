```markdown
### authorize_payment

```python
def authorize_payment(amount: float, currency: str = "USD", capture_method: str = "automatic", idempotency_key: str | None = None) -> dict
```

Authorize a payment without capturing funds immediately.

Use `capture_method='manual'` to hold funds and capture later via `capture_payment()`.
Authorized but uncaptured payments expire after 7 days.

**Parameters:**

*   `amount` (float): The amount to authorize.
*   `currency` (str, optional): The currency for the payment (e.g., "USD", "EUR"). Defaults to "USD".
*   `capture_method` (str, optional):  `"automatic"` to immediately capture funds, or `"manual"` to authorize only. Defaults to `"automatic"`.
*   `idempotency_key` (str | None, optional):  A unique key to prevent duplicate authorizations. If provided, repeated calls with the same key will return the same authorization. Defaults to `None`.

**Returns:**

A dictionary containing the authorization details:

*   `transaction_id` (str):  A unique transaction identifier (starts with "txn\_auth\_").
*   `status` (str): The status of the authorization, which will be `"authorized"`.
*   `amount` (float): The authorized amount.
*   `currency` (str): The currency of the authorization.
*   `capture_method` (str): The capture method used.

**Example:**

```python
authorization = authorize_payment(amount=100.00, currency="USD", capture_method="manual")
print(authorization)
# Expected output (actual transaction_id will vary):
# {'transaction_id': 'txn_auth_new', 'status': 'authorized', 'amount': 100.0, 'currency': 'USD', 'capture_method': 'manual'}
```
```python
authorization = authorize_payment(amount=50.00, currency="EUR", idempotency_key="unique_key_123")
print(authorization)
# Expected output (actual transaction_id will vary):
# {'transaction_id': 'txn_auth_unique_key_123', 'status': 'authorized', 'amount': 50.0, 'currency': 'EUR', 'capture_method': 'automatic'}
```
