```markdown
### `apply_credit_83fb54` Function
```python
def apply_credit_83fb54(account_id: str, credit: float) -> dict:
    """Apply a credit to a customer account.

    Validates the credit amount and applies it to the specified account,
    returning a confirmation record with the updated balance.

    Args:
        account_id: Target account identifier.
        credit: Credit amount to apply (must be > 0).

    Returns:
        dict with account_id, applied_credit, and status keys.

    Raises:
        ValueError: if the credit amount is not positive.

    Example:
        >>> apply_credit_83fb54(account_id="acc-123", credit=50.0)
        {'account_id': 'acc-123', 'applied_credit': 50.0, 'status': 'ok'}
```

**Description:**

Apply a credit to a customer account. This function validates that the credit amount is positive and then simulates applying it to the specified account. It returns a confirmation dictionary containing the account ID, the applied credit amount, and a status indicating success.

**Parameters:**

*   `account_id` (str): The unique identifier for the customer account to which the credit will be applied.
*   `credit` (float): The amount of credit to apply. This value must be greater than zero.

**Returns:**

A dictionary containing:
*   `account_id` (str): The identifier of the account that received the credit.
*   `applied_credit` (float): The amount of credit that was applied.
*   `status` (str): The status of the operation, which will be "ok" upon successful application.

**Raises:**

*   `ValueError`: If the provided `credit` amount is less than or equal to zero.

**Example:**

```python
credit_confirmation = apply_credit_83fb54(account_id="acc-987", credit=75.50)
print(credit_confirmation)
# Expected output: {'account_id': 'acc-987', 'applied_credit': 75.50, 'status': 'ok'}
```
```