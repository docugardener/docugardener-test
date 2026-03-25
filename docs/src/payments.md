```markdown
### `init_payment`

Initiates a payment transaction.

**Parameters:**

-   `amount` (float): The amount to be paid.
-   `currency` (str, optional): The currency of the payment. Defaults to `"USD"`.

**Returns:**

dict: A dictionary containing the transaction ID, status, and currency.

**Example:**

```python
result = init_payment(amount=100.0, currency="EUR")
print(result)
# Expected output: {'transaction_id': 'txn_123', 'status': 'pending', 'currency': 'EUR'}
```
```