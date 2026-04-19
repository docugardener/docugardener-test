### `apply_surcharge_c23a79`
Applies a percentage-based surcharge to a payment transaction.

This function calculates the surcharge value based on a given percentage, validates the input parameters, and returns a detailed breakdown of the transaction. The surcharge percentage must be strictly between 0 and 50.

Args:
    amount (float): The base transaction amount. Must be a positive value.
    surcharge_pct (float): The surcharge rate expressed as a percentage (e.g., 2.5 for 2.5%).
    currency (str, optional): The ISO 4217 currency code for the transaction. Defaults to "USD".

Returns:
    dict: A dictionary containing the surcharge breakdown:
        * `"original"` (float): The original transaction amount.
        * `"surcharge"` (float): The calculated surcharge amount, rounded to 2 decimal places.
        * `"total"` (float): The total amount including the surcharge, rounded to 2 decimal places.
        * `"currency"` (str): The currency code applied to the transaction.
        * `"rate_applied"` (float): The surcharge percentage that was applied.

Raises:
    ValueError: If `amount` is not positive, or if `surcharge_pct` is not between 0 and 50 (exclusive).

Example:
```python
surcharge_details = apply_surcharge_c23a79(
    amount=100.00,
    surcharge_pct=2.5,
    currency="EUR"
)
print(surcharge_details)
# Output: {'original': 100.0, 'surcharge': 2.5, 'total': 102.5, 'currency': 'EUR', 'rate_applied': 2.5}

try:
    apply_surcharge_c23a79(amount=50.0, surcharge_pct=60.0)
except ValueError as e:
    print(e)
# Output: surcharge_pct must be between 0 and 50
```