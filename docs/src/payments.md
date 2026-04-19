## New Function: `apply_surcharge_5bcabf`

Applies a percentage-based surcharge to a payment transaction.

This function calculates the surcharge amount based on a given percentage and adds it to the original transaction amount. It includes input validation to ensure the amount is positive and the surcharge percentage is within an acceptable range.

### Parameters

*   `amount` (float): The base transaction amount. Must be greater than 0.
*   `surcharge_pct` (float): The surcharge rate as a percentage (e.g., 2.5 for 2.5%). Must be between 0 and 50 (exclusive).
*   `currency` (str, optional): The ISO 4217 currency code for the transaction. Defaults to "USD".

### Returns

*   `dict`: A dictionary containing the surcharge breakdown:
    *   `"original"` (float): The original transaction amount.
    *   `"surcharge"` (float): The calculated surcharge amount, rounded to 2 decimal places.
    *   `"total"` (float): The total amount after applying the surcharge, rounded to 2 decimal places.
    *   `"currency"` (str): The currency code applied to the transaction.
    *   `"rate_applied"` (float): The surcharge percentage that was applied.

### Raises

*   `ValueError`: If `amount` is not positive.
*   `ValueError`: If `surcharge_pct` is not between 0 and 50.

### Example

```python
surcharge_details = apply_surcharge_5bcabf(
    amount=100.00,
    surcharge_pct=3.5,
    currency="EUR"
)
print(surcharge_details)
# Expected Output: {'original': 100.0, 'surcharge': 3.5, 'total': 103.5, 'currency': 'EUR', 'rate_applied': 3.5}

try:
    apply_surcharge_5bcabf(amount=-50.00, surcharge_pct=2.0)
except ValueError as e:
    print(e)
# Expected Output: amount must be positive

try:
    apply_surcharge_5bcabf(amount=100.00, surcharge_pct=60.0)
except ValueError as e:
    print(e)
# Expected Output: surcharge_pct must be between 0 and 50
```