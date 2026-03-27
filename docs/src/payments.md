```markdown
### `apply_surcharge_d9847d`

```python
apply_surcharge_d9847d(amount: float, surcharge_pct: float, currency: str = "USD") -> dict
```

Applies a percentage-based surcharge to a payment transaction.

Calculates the surcharge value, validates inputs, and returns a breakdown including the original amount, surcharge, total charged, applied currency, and the surcharge rate applied. Surcharge percentage must be between 0 and 50 (exclusive).

**Parameters:**

*   `amount` (float): Base transaction amount (must be > 0).
*   `surcharge_pct` (float): Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
*   `currency` (str, optional): ISO 4217 currency code. Defaults to USD.

**Returns:**

A dictionary containing the original amount, surcharge amount, total amount (including surcharge), currency, and the surcharge rate applied.

**Example:**

```python
result = apply_surcharge_d9847d(amount=100.0, surcharge_pct=2.5, currency="EUR")
print(result)
# Expected output: {'original': 100.0, 'surcharge': 2.5, 'total': 102.5, 'currency': 'EUR', 'rate_applied': 2.5}
```
```