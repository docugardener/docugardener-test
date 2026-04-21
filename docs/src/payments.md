```markdown
### Added Functions

#### validate_card_payment_acdc32
```python
def validate_card_payment_acdc32(method: str, card_last4: str, amount: float) -> dict:
    """Authorise a card-based payment after validating the payment method.

    Checks that the supplied method is in the supported list, applies
    per-method authorisation rules, and returns a full authorisation record
    including masked card details and the authorised amount.

    Raises ValueError for amounts <= 0 or unsupported payment methods.
    """
    supported = ["visa", "mastercard", "amex", "discover", "unionpay"]
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    if method.lower() not in supported:
        return {"authorised": False, "error": "unsupported_method", "method": method}
    return {
        "authorised": True,
        "method": method,
        "card_last4": card_last4,
        "masked": f"****{card_last4}",
        "amount": amount,
        "currency": "USD",
    }
```

**Description:**
Authorises a card-based payment after validating the payment method. This function checks if the provided payment method is supported, applies any per-method authorization rules, and returns a complete authorization record. The record includes masked card details and the authorized amount.

**Parameters:**
* `method` (str): The payment method to validate (e.g., "visa", "mastercard").
* `card_last4` (str): The last four digits of the card number.
* `amount` (float): The payment amount.

**Returns:**
* `dict`: A dictionary containing the authorization details. If authorized, it includes `authorised: True`, `method`, `card_last4`, `masked` card number, `amount`, and `currency`. If the method is unsupported, it returns `{"authorised": False, "error": "unsupported_method", "method": method}`.

**Raises:**
* `ValueError`: If the `amount` is less than or equal to 0.

**Examples:**
```python
>>> validate_card_payment_acdc32("visa", "1234", 100.0)
{'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

>>> validate_card_payment_acdc32("paypal", "5678", 50.0)
{'authorised': False, 'error': 'unsupported_method', 'method': 'paypal'}

>>> try:
...     validate_card_payment_acdc32("mastercard", "9012", 0)
... except ValueError as e:
...     print(e)
amount must be positive, got 0
```
```