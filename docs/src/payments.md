```markdown
### `apply_surcharge_9719b7`
Applies a percentage-based surcharge to a payment transaction.

Calculates the surcharge value, validates inputs, and returns a breakdown
including the original amount, surcharge, total charged, and applied currency.
Surcharge percentage must be between 0 and 50 (exclusive).

**Parameters:**

*   `amount` (float): Base transaction amount (must be > 0).
*   `surcharge_pct` (float): Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
*   `currency` (str): ISO 4217 currency code. Defaults to "USD".

**Returns:**

*   `dict`: A dictionary containing the original amount, surcharge amount, total amount charged, and the currency.

**Raises:**

*   `ValueError`: If `amount` is not positive.
*   `ValueError`: If `surcharge_pct` is not between 0 and 50.

**Example:**

```python
original_amount = 100.0
surcharge_rate = 5.0
result = apply_surcharge_9719b7(original_amount, surcharge_rate, "EUR")
print(result)
# Expected output: {'original': 100.0, 'surcharge': 5.0, 'total': 105.0, 'currency': 'EUR', 'rate_applied': 5.0}
```
```