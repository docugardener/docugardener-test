```markdown
### `apply_surcharge_c31709`

Applies a percentage-based surcharge to a payment transaction.

Calculates the surcharge value, validates inputs, and returns a breakdown including the original amount, surcharge, total charged, applied currency, and the surcharge rate applied. The surcharge percentage must be between 0 and 50 (exclusive).

**Parameters:**

*   `amount` (float): Base transaction amount (must be > 0).
*   `surcharge_pct` (float): Surcharge rate as a percentage (e.g., 2.5 for 2.5%).
*   `currency` (str, optional): ISO 4217 currency code. Defaults to "USD".

**Returns:**

dict: A dictionary containing the original amount, surcharge amount, total amount (including surcharge), currency, and the surcharge rate applied.

**Example:**

```python
result = apply_surcharge_c31709(amount=100.0, surcharge_pct=5.0, currency="EUR")
print(result)
# Expected output (approximately):
# {'original': 100.0, 'surcharge': 5.0, 'total': 105.0, 'currency': 'EUR', 'rate_applied': 5.0}
```
```