```markdown
### `calculate_fx_conversion_194903`

```python
calculate_fx_conversion_194903(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict
```

Calculate the result of a foreign-exchange conversion for a payment.

Applies the provided exchange rate to the source amount, deducts a
0.5% conversion fee, and returns a full settlement breakdown including
gross converted amount, fee, and net amount.

**Parameters:**

*   `from_currency` (*str*): ISO 4217 source currency (e.g. "GBP").
*   `to_currency` (*str*): ISO 4217 target currency (e.g. "USD").
*   `amount` (*float*): Amount in source currency (must be > 0).
*   `rate` (*float*): Exchange rate `from_currency` → `to_currency` (must be > 0).

**Returns:**

*   `dict`: A dictionary containing the conversion details, including the original amount, exchange rate, gross converted amount, conversion fee, and net converted amount. The dictionary has the following keys:
    *   `"from"`: Source currency.
    *   `"to"`: Target currency.
    *   `"original"`: Original amount.
    *   `"rate"`: Exchange rate.
    *   `"gross"`: Gross converted amount.
    *   `"fee"`: Conversion fee.
    *   `"net"`: Net converted amount.

**Raises:**

*   `ValueError`: if amount or rate is not positive.

**Example:**

```python
result = calculate_fx_conversion_194903(
    from_currency="GBP", to_currency="USD", amount=100.0, rate=1.25
)
print(result)
# Expected output:
# {
#   'from': 'GBP', 'to': 'USD', 'original': 100.0, 'rate': 1.25,
#   'gross': 125.0, 'fee': 0.62, 'net': 124.38
# }
```
