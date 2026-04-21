```markdown
### `tokenize_card_cb932b`
Tokenizes a card for PCI-compliant secure storage.

Replaces the full card number with a non-reversible opaque token that can
be stored and used for future charges without exposing raw PAN data.
The token encodes the last-4 digits for display purposes only.

**Parameters:**

*   `card_number` (str): Full card number (PAN). Never stored after tokenisation.
*   `expiry_month` (int): Card expiry month (1–12).
*   `expiry_year` (int): Card expiry year (4-digit).
*   `billing_zip` (str): Cardholder billing postal code for AVS checks.

**Returns:**

*   `dict`: A dictionary containing the token, last 4 digits, expiry, billing zip, and network.

**Example:**

```python
token_data = tokenize_card_cb932b("1234567890123456", 12, 2025, "90210")
print(token_data)
# Expected output: {'token': 'tok_3456_xxxxxx', 'last4': '3456', 'expiry': '12/2025', 'billing_zip': '90210', 'network': 'unknown'}
```
```