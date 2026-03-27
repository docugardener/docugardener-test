```markdown
Adds the `tokenize_card` function to tokenize card details.

### `tokenize_card`

```python
def tokenize_card(
    card_number: str,
    expiry: str,
    cvv: str,
) -> dict:
```

Tokenize a card for future payments.

Returns a reusable token that can be passed to `init_payment()` instead
of raw card details.

**Parameters:**

*   `card_number` (str): The card number to tokenize.
*   `expiry` (str): The card expiry date (MM/YY).
*   `cvv` (str): The card CVV.

**Returns:**

*   dict: A dictionary containing the tokenized card details.

**Example:**

```python
tokenize_card(
    card_number="4111111111111111",
    expiry="12/24",
    cvv="123",
)
# Returns: {'token': 'tok_new', 'last4': '1111', 'expiry': '12/24', 'status': 'active'}
```
