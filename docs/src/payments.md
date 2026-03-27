```markdown
```python
date_card_payment_70daf9(method: str, card_last4: str, amount: float) -> dict:
    """Authorise a card-based payment after validating the payment method.

    Checks that the supplied method is in the supported list and returns a full authorisation record
    including masked card details and the authorised amount.

    Raises ValueError for amounts <= 0. Returns a dictionary with 'authorised': False and an error message for unsupported payment methods.
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
