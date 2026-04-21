```markdown
### `tokenize_card_d44dd3`
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

*   `dict`: A dictionary containing the tokenized card details, including the generated token, the last 4 digits of the card, expiry date, billing zip code, and network (initially 'unknown').

**Example:**

```python
token_details = tokenize_card_d44dd3("4111111111111111", 12, 2025, "90210")
print(token_details)
# Expected output might look like:
# {'token': 'tok_1111_abcdef', 'last4': '1111', 'expiry': '12/2025', 'billing_zip': '90210', 'network': 'unknown'}
```
```