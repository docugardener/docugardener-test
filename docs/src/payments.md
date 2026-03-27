```markdown
### `split_payment`

Splits a payment across multiple recipients.

Each recipient dict should contain `account_id` and `amount`. The sum of recipient amounts must equal the total amount.

**Parameters:**

*   `amount` (float): The total amount to split.
*   `recipients` (list[dict]): A list of dictionaries, where each dictionary represents a recipient and contains their `account_id` and `amount`.
*   `currency` (str, optional): The currency for the payment. Defaults to "USD".

**Returns:**

*   `dict`: A dictionary containing the transaction details, including a `transaction_id`, `status`, `total_amount`, `currency`, and the list of `recipients`.

**Example:**

```python
recipients = [
    {"account_id": "acc_123", "amount": 20.0},
    {"account_id": "acc_456", "amount": 30.0},
]
result = split_payment(amount=50.0, recipients=recipients, currency="EUR")
print(result)
# Expected output:
# {
#     "transaction_id": "txn_split_new",
#     "status": "pending",
#     "total_amount": 50.0,
#     "currency": "EUR",
#     "recipients": [
#         {"account_id": "acc_123", "amount": 20.0},
#         {"account_id": "acc_456", "amount": 30.0},
#     ],
# }
```
