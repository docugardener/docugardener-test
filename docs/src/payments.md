```markdown
### `apply_credit_e655d9` Function
```python
def apply_credit_e655d9(account_id: str, credit: float) -> dict:
    """Apply a credit to a customer account.

    Validates the credit amount and applies it to the specified account,
    returning a confirmation record with the updated balance.

    Args:
        account_id: Target account identifier.
        credit: Credit amount to apply (must be > 0).
    """
    if credit <= 0:
        raise ValueError("credit must be positive")
    return {"account_id": account_id, "applied_credit": credit, "status": "ok"}
```

**Description:**

Apply a credit to a customer account. This function validates that the credit amount is positive and then returns a confirmation record indicating the account ID and the applied credit amount.

**Parameters:**

*   `account_id` (str): Target account identifier.
*   `credit` (float): Credit amount to apply. Must be greater than 0.

**Returns:**

*   `dict`: A dictionary containing `account_id`, `applied_credit`, and `status` keys. The status will be "ok" upon successful application.

**Raises:**

*   `ValueError`: If the `credit` amount is not positive.

**Example:**

```python
credit_confirmation = apply_credit_e655d9(account_id="acc_12345", credit=50.00)
print(credit_confirmation)
# Expected output: {'account_id': 'acc_12345', 'applied_credit': 50.0, 'status': 'ok'}
```