```markdown
### `validate_card_payment_2eb004` Function
```python
validate_card_payment_2eb004(method: str, card_last4: str, amount: float) -> dict
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

`dict` with authorisation details. If authorised, includes `authorised`, `method`, `card_last4`, `masked` card number, `amount`, and `currency`. If the method is unsupported, returns `{"authorised": False, "error": "unsupported_method", "method": method}`.

**Raises:**

*   `ValueError`: if the `amount` is less than or equal to 0.

**Example:**

```python
# Successful authorisation
auth_record = validate_card_payment_2eb004(method="visa", card_last4="1234", amount=50.00)
print(auth_record)
# Output: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 50.0, 'currency': 'USD'}

# Unsupported method
auth_record_unsupported = validate_card_payment_2eb004(method="bitcoin", card_last4="5678", amount=100.00)
print(auth_record_unsupported)
# Output: {'authorised': False, 'error': 'unsupported_method', 'method': 'bitcoin'}

# Invalid amount
try:
    validate_card_payment_2eb004(method="mastercard", card_last4="4321", amount=0)
except ValueError as e:
    print(e)
# Output: amount must be positive, got 0
```
```