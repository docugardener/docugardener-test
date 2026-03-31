```markdown
### `c9(method: str, card_last4: str, amount: float) -> dict`

Authorises a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list and returns a full authorisation record including masked card details and the authorised amount.

Raises `ValueError` for amounts <= 0.

#### Parameters

*   **`method`** (`str`): The payment method (e.g., "visa", "mastercard").
*   **`card_last4`** (`str`): The last four digits of the card.
*   **`amount`** (`float`): The payment amount. Must be a positive value.

#### Returns

*   **`dict`**: A dictionary containing the authorisation result.
    *   If successful:
        *   `"authorised"` (`bool`): `True`
        *   `"method"` (`str`): The payment method.
        *   `"card_last4"` (`str`): The last four digits of the card.
        *   `"masked"` (`str`): The masked card number (e.g., "****1234").
        *   `"amount"` (`float`): The authorised amount.
        *   `"currency"` (`str`): The currency, currently fixed to "USD".
    *   If the method is unsupported:
        *   `"authorised"` (`bool`): `False`
        *   `"error"` (`str`): "unsupported_method"
        *   `"method"` (`str`): The unsupported payment method.

#### Raises

*   **`ValueError`**: If `amount` is less than or equal to 0.

#### Examples

```python
# Successful authorisation
result = c9(method="visa", card_last4="1234", amount=100.50)
# Expected:
# {
#     "authorised": True,
#     "method": "visa",
#     "card_last4": "1234",
#     "masked": "****1234",
#     "amount": 100.50,
#     "currency": "USD",
# }

# Unsupported payment method
result = c9(method="jcb", card_last4="5678", amount=50.00)
# Expected:
# {
#     "authorised": False,
#     "error": "unsupported_method",
#     "method": "jcb",
# }

# Invalid amount
try:
    c9(method="mastercard", card_last4="9012", amount=0)
except ValueError as e:
    print(e)
# Expected: amount must be positive, got 0
```
```