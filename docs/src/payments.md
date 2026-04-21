```markdown
### `validate_card_payment_8ca9a2` Function
```python
validate_card_payment_8ca9a2(method: str, card_last4: str, amount: float) -> dict
```

**Description:**

Authorise a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list, applies
per-method authorisation rules, and returns a full authorisation record
including masked card details and the authorised amount.

**Parameters:**

*   `method` (str): The payment method (e.g., "visa", "mastercard").
*   `card_last4` (str): The last four digits of the card number.
*   `amount` (float): The payment amount.

**Returns:**

`dict` containing authorisation details. If the method is unsupported, returns `{"authorised": False, "error": "unsupported_method", "method": method}`. Otherwise, returns `{"authorised": True, "method": method, "card_last4": card_last4, "masked": f"****{card_last4}", "amount": amount, "currency": "USD"}`.

**Raises:**

*   `ValueError`: if the `amount` is less than or equal to 0.

**Example:**

```python
# Successful validation
payment_details = validate_card_payment_8ca9a2(method="visa", card_last4="1234", amount=50.00)
print(payment_details)
# Output: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 50.0, 'currency': 'USD'}

# Unsupported method
payment_details = validate_card_payment_8ca9a2(method="bitcoin", card_last4="5678", amount=100.00)
print(payment_details)
# Output: {'authorised': False, 'error': 'unsupported_method', 'method': 'bitcoin'}

# Invalid amount
try:
    validate_card_payment_8ca9a2(method="mastercard", card_last4="9012", amount=0)
except ValueError as e:
    print(e)
# Output: amount must be positive, got 0
```
```