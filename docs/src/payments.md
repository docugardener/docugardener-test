### `create_payment`
Create a new payment transaction.

**Parameters:**

*   `amount` (float, required) — payment amount
*   `currency` (str, optional) — currency of the payment. Defaults to "USD".
*   `customer_id` (str | None, optional) — identifier for the customer making the payment.

**Returns:**

*   dict: A dictionary containing the transaction ID, status, currency, and customer ID.

**Example:**

```python
payment_details = create_payment(amount=100.0, currency="EUR", customer_id="cust_abc")
print(payment_details)
# Output: {'transaction_id': 'txn_123', 'status': 'pending', 'currency': 'EUR', 'customer_id': 'cust_abc'}

payment_details_no_customer = create_payment(amount=50.0)
print(payment_details_no_customer)
# Output: {'transaction_id': 'txn_123', 'status': 'pending', 'currency': 'USD', 'customer_id': None}
```