### `validate_card_payment_24003d` Function
```python
validate_card_payment_24003d(method: str, card_last4: str, amount: float) -> dict
```

**Description:**

Authorise a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list, applies per-method authorisation rules, and returns a full authorisation record including masked card details and the authorised amount.

**Parameters:**

*   `method` (str): The payment method (e.g., "visa", "mastercard").
*   `card_last4` (str): The last four digits of the card number.
*   `amount` (float): The payment amount.

**Returns:**

*   A dictionary containing authorisation details if the payment is successful. This includes `authorised` (True), `method`, `card_last4`, `masked` card number, `amount`, and `currency`.
*   A dictionary with `authorised` set to `False`, an `error` key (e.g., "unsupported_method"), and the provided `method` if the payment method is not supported.

**Raises:**

*   `ValueError`: if the `amount` is less than or equal to 0.

**Example:**

```python
# Successful payment
auth_success = validate_card_payment_24003d(method="visa", card_last4="1234", amount=100.00)
print(auth_success)
# Expected output: {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

# Unsupported payment method
auth_unsupported = validate_card_payment_24003d(method="bitcoin", card_last4="5678", amount=50.00)
print(auth_unsupported)
# Expected output: {'authorised': False, 'error': 'unsupported_method', 'method': 'bitcoin'}

# Invalid amount
try:
    validate_card_payment_24003d(method="mastercard", card_last4="5678", amount=0)
except ValueError as e:
    print(e)
# Expected output: amount must be positive, got 0
```