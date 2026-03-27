```markdown
### `create_payment_link`

```python
def create_payment_link(
    amount: float,
    currency: str = "USD",
    expires_in_hours: int = 24,
    metadata: dict | None = None,
) -> dict:
```

Generate a shareable payment link for a given amount.

The link expires after `expires_in_hours` (default 24h).
Optional `metadata` is attached to the resulting transaction.

**Parameters:**

-   `amount` (float): The payment amount.
-   `currency` (str, optional): The currency for the payment (default: "USD").
-   `expires_in_hours` (int, optional): The link's expiration time in hours (default: 24).
-   `metadata` (dict | None, optional): Optional metadata to attach to the transaction (default: None).

**Returns:**

-   `dict`: A dictionary containing the payment link and details.

**Example:**

```python
result = create_payment_link(amount=100.00, currency="EUR", expires_in_hours=48, metadata={"order_id": "123"})
print(result)
# Expected output:
# {
#     "payment_link": "https://pay.example.com/link_new",
#     "amount": 100.00,
#     "currency": "EUR",
#     "expires_in_hours": 48,
#     "status": "active",
# }
```
```