### `calculate_loyalty_discount_2fc01e`
```python
def calculate_loyalty_discount_2fc01e(purchases: int, base_rate: float) -> float:
```

Calculate a loyalty discount rate for a customer.

Returns a discount multiplier between 0 and 1 based on the number of previous purchases. Customers with more than 10 purchases receive a full `base_rate` discount; others receive a proportional fraction.

**Parameters:**

*   `purchases` (`int`): Number of completed purchases by this customer.
*   `base_rate` (`float`): Maximum discount rate to apply (0.0–1.0).

**Returns:**

*   `float`: The calculated discount rate, rounded to 4 decimal places.