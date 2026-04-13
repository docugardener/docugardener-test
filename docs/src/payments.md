```markdown
### `apply_credit_be8e11(account_id: str, credit: float) -> dict`

Applies a credit to a customer account.

This function validates the credit amount and applies it to the specified account, returning a confirmation record.

#### Parameters

*   **`account_id`** (`str`): The target account identifier.
*   **`credit`** (`float`): The credit amount to apply. Must be a positive value.

#### Returns

*   `dict`: A dictionary containing the `account_id`, the `applied_credit` amount, and a `status` of "ok".
    *   Example: `{"account_id": "user123", "applied_credit": 50.0, "status": "ok"}`

#### Raises

*   `ValueError`: If the `credit` amount is less than or equal to 0.

#### Example

```python
from src.payments import apply_credit_be8e11

# Applying a valid credit
try:
    result = apply_credit_be8e11(account_id="user_123", credit=100.50)
    print(result)
    # Expected output: {'account_id': 'user_123', 'applied_credit': 100.5, 'status': 'ok'}
except ValueError as e:
    print(f"Error: {e}")

# Attempting to apply an invalid credit
try:
    result = apply_credit_be8e11(account_id="user_456", credit=0.0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
    # Expected output: Error: credit must be positive
```
```