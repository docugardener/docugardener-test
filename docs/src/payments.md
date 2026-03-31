```markdown
### `apply_surcharge_338fd4`

```python
def apply_surcharge_338fd4(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
```

Apply a percentage-based surcharge to a payment transaction.

Calculates the surcharge value, validates inputs, and returns a breakdown including the original amount, surcharge, total charged, and applied currency. Surcharge percentage must be between 0 and 50 (exclusive).

#### Parameters

*   **`amount`** (`float`):
    Base transaction amount. Must be greater than 0.
*   **`surcharge_pct`** (`float`):
    Surcharge rate as a percentage (e.g., `2.5` for 2.5%). Must be between 0 and 50 (exclusive).
*   **`currency`** (`str`, *optional*):
    ISO 4217 currency code. Defaults to `"USD"`.

#### Returns

*   **`dict`**:
    A dictionary containing the transaction breakdown:
    *   `"original"` (`float`): The base transaction amount.
    *   `"surcharge"` (`float`): The calculated surcharge amount, rounded to two decimal places.
    *   `"total"` (`float`): The total amount charged (original + surcharge), rounded to two decimal places.
    *   `"currency"` (`str`): The currency code applied.
    *   `"rate_applied"` (`float`): The surcharge percentage rate that was applied.

#### Raises

*   **`ValueError`**:
    *   If `amount` is not positive.
    *   If `surcharge_pct` is not between 0 and 50 (exclusive).

#### Example

```python
# Apply a 2.5% surcharge to $100
result_usd = apply_surcharge_338fd4(amount=100.00, surcharge_pct=2.5)
# result_usd will be:
# {
#     "original": 100.0,
#     "surcharge": 2.5,
#     "total": 102.5,
#     "currency": "USD",
#     "rate_applied": 2.5
# }

# Apply a 5% surcharge in EUR
result_eur = apply_surcharge_338fd4(amount=50.00, surcharge_pct=5.0, currency="EUR")
# result_eur will be:
# {
#     "original": 50.0,
#     "surcharge": 2.5,
#     "total": 52.5,
#     "currency": "EUR",
#     "rate_applied": 5.0
# }

# Example of invalid input
try:
    apply_surcharge_338fd4(amount=0, surcharge_pct=10)
except ValueError as e:
    print(e) # Output: amount must be positive

try:
    apply_surcharge_338fd4(amount=100, surcharge_pct=55)
except ValueError as e:
    print(e) # Output: surcharge_pct must be between 0 and 50
```
```