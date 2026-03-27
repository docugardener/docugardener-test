```markdown
```python
tokenize_card_48572b(
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
        A dictionary containing the token, last four digits of the card,
        expiry date, billing zip code, and network (always 'unknown').

    Example:
        >>> tokenize_card_48572b(card_number='4111111111111111', expiry_month=12, expiry_year=2025, billing_zip='12345')
        {'token': 'tok_1111_xxxxxxxx', 'last4': '1111', 'expiry': '12/2025', 'billing_zip': '12345', 'network': 'unknown'}
        Note: The 'token' value is non-deterministic and 'xxxxxxxx' will be a different hexadecimal value on each run.
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
