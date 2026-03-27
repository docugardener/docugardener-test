```markdown
Adds the `batch_payment` function to submit multiple payment transactions as a single batch.

### `batch_payment`

```python
def batch_payment(
    transactions: list[dict],
    currency: str = "USD",
) -> dict:
```

Submit multiple payment transactions as a single batch.

Each transaction dict must contain 'amount' and 'recipient_id'.
All transactions in a batch share the same currency.

**Parameters:**

*   `transactions` (list[dict]): A list of transaction dictionaries, each containing 'amount' and 'recipient_id'.
*   `currency` (str, optional): The currency for all transactions in the batch. Defaults to "USD".

**Returns:**

*   dict: A dictionary containing the batch ID, status, transaction count, and currency.

**Example:**

```python
transactions = [
    {"amount": 10, "recipient_id": "user1"},
    {"amount": 20, "recipient_id": "user2"},
]
result = batch_payment(transactions, currency="EUR")
print(result)
# Expected output: {'batch_id': 'batch_new', 'status': 'processing', 'transaction_count': 2, 'currency': 'EUR'}
```
```