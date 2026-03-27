```markdown
### `validate_card_payment_a9eaaa`

```python
validate_card_payment_a9eaaa(method: str, card_last4: str, amount: float) -> dict:
```

Authorise a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list and returns a full authorisation record
including masked card details and the authorised amount.

Raises `ValueError` for amounts less than or equal to 0. Returns a dictionary with `authorised: False` and an error message if the payment method is not supported.

**Parameters:**

*   `method` (str): The payment method (e.g., "visa", "mastercard").
*   `card_last4` (str): The last four digits of the card number.
*   `amount` (float): The payment amount.

**Returns:**

A dictionary containing the authorisation details. If the payment is authorised, the dictionary will contain `authorised: True`, the payment `method`, the `card_last4`, a masked card number, the `amount`, and the `currency`. If the payment is not authorised (due to an unsupported method), the dictionary will contain `authorised: False`, an `error` message, and the attempted `method`.

**Raises:**

*   `ValueError`: if `amount` is less than or equal to 0.

**Examples:**

```python
# Successful authorisation
result = validate_card_payment_a9eaaa(method="visa", card_last4="1234", amount=100.0)
print(result)
# Expected output: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

# Unsuccessful authorisation due to unsupported method
result = validate_card_payment_a9eaaa(method="unsupported", card_last4="1234", amount=100.0)
print(result)
# Expected output: {'authorised': False, 'error': 'unsupported_method', 'method': 'unsupported'}

# Unsuccessful authorisation due to non-positive amount
try:
    result = validate_card_payment_a9eaaa(method="visa", card_last4="1234", amount=-100.0)
except ValueError as e:
    print(e)
# Expected output: amount must be positive, got -100.0
```
