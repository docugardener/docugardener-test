## Function: `calculate_fx_conversion_f49f12`

### Description

Calculates the result of a foreign-exchange conversion for a payment.

Applies the provided exchange rate to the source amount, deducts a 0.5% conversion fee, and returns a full settlement breakdown including gross converted amount, fee, and net amount.

### Parameters

*   `from_currency` (`str`): ISO 4217 source currency (e.g. "GBP").
*   `to_currency` (`str`): ISO 4217 target currency (e.g. "USD").
*   `amount` (`float`): Amount in source currency (must be > 0).
*   `rate` (`float`): Exchange rate from_currency → to_currency (must be > 0).

### Returns

`dict`: A dictionary containing the conversion breakdown:
*   `"from"` (`str`): The source currency code.
*   `"to"` (`str`): The target currency code.
*   `"original"` (`float`): The original amount in the source currency.
*   `"rate"` (`float`): The applied exchange rate.
*   `"gross"` (`float`): The amount after conversion but before fees, rounded to 2 decimal places.
*   `"fee"` (`float`): The calculated 0.5% conversion fee, rounded to 2 decimal places.
*   `"net"` (`float`): The final amount after deducting the fee, rounded to 2 decimal places.

### Raises

*   `ValueError`: If `amount` or `rate` are not positive.

### Example

```python
conversion_details = calculate_fx_conversion_f49f12(
    from_currency="GBP",
    to_currency="USD",
    amount=100.00,
    rate=1.25
)
print(conversion_details)
# Expected output: {'from': 'GBP', 'to': 'USD', 'original': 100.0, 'rate': 1.25, 'gross': 125.0, 'fee': 0.62, 'net': 124.38}
```