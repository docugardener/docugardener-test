```markdown
### `tokenize_card_d18a9b`

```python
def tokenize_card_d18a9b(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
```

Tokenize a card for PCI-compliant secure storage.

Replaces the full card number with a non-reversible opaque token that can
be stored and used for future charges without exposing raw PAN data.
The token encodes the last-4 digits for display purposes only.

**Parameters:**

*   `card_number` (str): Full card number (PAN). Never stored after tokenisation.
*   `expiry_month` (int): Card expiry month (1–12).
*   `expiry_year` (int): Card expiry year (4-digit).
*   `billing_zip` (str): Cardholder billing postal code for AVS checks.

**Returns:**

A dictionary containing the tokenized card details.

**Example:**

```python
result = tokenize_card_d18a9b(
    card_number="4111111111111111",
    expiry_month=12,
    expiry_year=2025,
    billing_zip="90210",
)
print(result)
# Expected output (token value will vary):
# {
#     'token': 'tok_1111_abcdef',
#     'last4': '1111',
#     'expiry': '12/2025',
#     'billing_zip': '90210',
#     'network': 'unknown'
# }
```
