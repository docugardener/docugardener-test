```markdown
```python
def validate_card_payment_961c8a(method: str, card_last4: str, amount: float) -> dict:
    """Authorise a card-based payment after validating the payment method.

    Checks that the supplied method is in the supported list and returns
    an authorisation record including masked card details and the authorised
    amount.

    Raises ValueError for amounts <= 0.

    Parameters:
        method (str): The payment method (e.g., "visa", "mastercard").
        card_last4 (str): The last four digits of the card number.
        amount (float): The payment amount.

    Returns:
        dict: A dictionary containing the authorisation details.
            If the payment is authorised, the dictionary will contain:
                - authorised (bool): True
                - method (str): The payment method.
                - card_last4 (str): The last four digits of the card.
                - masked (str): The masked card number.
                - amount (float): The payment amount.
                - currency (str): The currency ("USD").
            If the payment is not authorised (unsupported method), the dictionary will contain:
                - authorised (bool): False
                - error (str): "unsupported_method"
                - method (str): The payment method.

    Raises:
        ValueError: If the amount is not positive.

    Example:
        >>> validate_card_payment_961c8a(method="visa", card_last4="1234", amount=100.0)
        {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

    Example:
        >>> validate_card_payment_961c8a(method="invalid", card_last4="1234", amount=100.0)
        {'authorised': False, 'error': 'unsupported_method', 'method': 'invalid'}

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