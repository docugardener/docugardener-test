```markdown
### `validate_card_payment_c7b0b7` Function
```python
validate_card_payment_c7b0b7(method: str, card_last4: str, amount: float) -> dict
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

`dict` containing the authorisation status, method, masked card details, and amount. If the method is unsupported, returns `{"authorised": False, "error": "unsupported_method", "method": method}`.

**Raises:**

*   `ValueError`: if the `amount` is less than or equal to 0.

**Example:**

```python
# Successful authorisation
auth_success = validate_card_payment_c7b0b7(method="visa", card_last4="1234", amount=50.00)
print(auth_success)
# Output: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 50.0, 'currency': 'USD'}

# Unsupported method
auth_fail = validate_card_payment_c7b0b7(method="paypal", card_last4="5678", amount=75.00)
print(auth_fail)
# Output: {'authorised': False, 'error': 'unsupported_method', 'method': 'paypal'}

# Invalid amount
try:
    validate_card_payment_c7b0b7(method="mastercard", card_last4="9012", amount=0)
except ValueError as e:
    print(e)
# Output: amount must be positive, got 0
```
```