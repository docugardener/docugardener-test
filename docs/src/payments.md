```markdown
### `send_receipt`

```python
def send_receipt(transaction_id: str, email: str, format: str = "html") -> dict
```

Send a payment receipt to a customer email address.

Supported formats: `'html'` (default), `'pdf'`, `'plain'`.
Returns delivery status and message ID.

**Parameters:**

-   `transaction_id` (*str*): The ID of the transaction.
-   `email` (*str*): The customer's email address.
-   `format` (*str*, optional): The format of the receipt. Defaults to `"html"`.

**Returns:**

*dict*: A dictionary containing the transaction ID, email, format, status, and message ID.

**Example:**

```python
result = send_receipt(transaction_id="tx_123", email="customer@example.com", format="pdf")
print(result)
# Expected output: {'transaction_id': 'tx_123', 'email': 'customer@example.com', 'format': 'pdf', 'status': 'sent', 'message_id': 'msg_new'}
```
