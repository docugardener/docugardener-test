```markdown
## tokenize_card_45d95a

Tokenize a card for PCI-compliant secure storage.

Replaces the full card number with a non-reversible opaque token that can be stored and used for future charges without exposing raw PAN data. The token encodes the last-4 digits for display purposes only.

### Parameters

*   `card_number` (str): Full card number (PAN). Never stored after tokenisation.
*   `expiry_month` (int): Card expiry month (1–12).
*   `expiry_year` (int): Card expiry year (4-digit).
*   `billing_zip` (str): Cardholder billing postal code for AVS checks.

### Returns

*   dict: A dictionary containing the tokenized card details:
    *   `token` (str): The generated opaque token.
    *   `last4` (str): The last 4 digits of the card number.
    *   `expiry` (str): The card expiry date in MM/YYYY format.
    *   `billing_zip` (str): The provided billing zip code.
    *   `network` (str): The card network (initially 'unknown').

### Example

```python
tokenize_card_45d95a("1234567890123456", 12, 2025, "90210")
# Output: {'token': 'tok_3456_abcdef', 'last4': '3456', 'expiry': '12/2025', 'billing_zip': '90210', 'network': 'unknown'}
```
```