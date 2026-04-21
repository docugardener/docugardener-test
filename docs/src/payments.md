### `validate_card_payment_3dd8c9` Function
```python
validate_card_payment_3dd8c9(method: str, card_last4: str, amount: float) -> dict
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

A dictionary containing the authorisation status, method, masked card details, and authorised amount. If the method is unsupported, it returns `{"authorised": False, "error": "unsupported_method", "method": method}`.

**Raises:**

*   `ValueError`: if the `amount` is less than or equal to 0.

**Example:**

```python
# Successful authorisation
auth_success = validate_card_payment_3dd8c9(method="visa", card_last4="1234", amount=100.00)
print(auth_success)
# Output: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

# Unsupported method
auth_fail = validate_card_payment_3dd8c9(method="bitcoin", card_last4="5678", amount=50.00)
print(auth_fail)
# Output: {'authorised': False, 'error': 'unsupported_method', 'method': 'bitcoin'}

# Invalid amount
try:
    validate_card_payment_3dd8c9(method="mastercard", card_last4="9012", amount=0)
except ValueError as e:
    print(e)
# Output: amount must be positive, got 0
```