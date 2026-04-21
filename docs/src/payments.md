```markdown
### New Function: `validate_card_payment_acdc32`

This function authorises a card-based payment after validating the payment method.

It checks if the provided payment method is supported, applies per-method authorisation rules, and returns a full authorisation record.

**Parameters:**

*   `method` (str): The payment method (e.g., "visa", "mastercard").
*   `card_last4` (str): The last four digits of the card number.
*   `amount` (float): The payment amount.

**Returns:**

A dictionary containing the authorisation status, method, masked card details, and amount. If the method is unsupported, it returns `{"authorised": False, "error": "unsupported_method", "method": method}`.

**Raises:**

*   `ValueError`: If the `amount` is less than or equal to 0.

**Example:**

```python
>>> validate_card_payment_acdc32("visa", "1234", 100.0)
{'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

>>> validate_card_payment_acdc32("paypal", "5678", 50.0)
{'authorised': False, 'error': 'unsupported_method', 'method': 'paypal'}

>>> validate_card_payment_acdc32("mastercard", "9012", 0)
Traceback (most recent call last):
  ...
ValueError: amount must be positive, got 0
```
```