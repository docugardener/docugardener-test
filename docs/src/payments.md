```markdown
### `validate_payment_method(method: str, card_last4: str) -> dict`

Validates a payment method before authorization.

Checks if the provided payment method is within the supported list and returns a validation summary, including masked card details.

**Parameters:**

-   `method` (str): The payment method to validate (e.g., "visa", "mastercard").
-   `card_last4` (str): The last four digits of the card number.

**Returns:**

A dictionary containing the validation result. If the method is supported, the dictionary includes `valid`: `True`, the payment `method`, the `card_last4`, and a masked card number (`masked`). If the method is not supported, the dictionary includes `valid`: `False`, an `error` code (`unsupported_method`), and the provided `method`.

**Example:**

```python
result = validate_payment_method("visa", "1234")
print(result)
# Expected output: {'valid': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234'}

result = validate_payment_method("paypal", "1234")
print(result)
# Expected output: {'valid': False, 'error': 'unsupported_method', 'method': 'paypal'}
```
```