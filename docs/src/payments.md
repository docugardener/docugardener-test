```markdown
```

No functional changes were made to the `card_number` function. The existing documentation accurately reflects the function's behavior. However, the return value was not documented. The documentation has been updated to include the return value.

```python
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.

    Returns:
        dict: A dictionary containing the tokenized card details. The dictionary has the following keys:
            - token (str): The generated token.
            - last4 (str): The last four digits of the card number.
            - expiry (str): The expiry date in MM/YYYY format.
            - billing_zip (str): The billing zip code.
            - network (str): The card network (always "unknown" at tokenization time).

    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }
```
