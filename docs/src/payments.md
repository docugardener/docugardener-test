```markdown
### `calculate_surcharge`

```python
def calculate_surcharge(
    amount: float,
    region: str,
    payment_method: str = "card",
) -> dict:
```

Calculates any applicable surcharge for a payment in a given region.

Some regions impose legal surcharge limits; this method returns the allowed surcharge amount and the applicable regulatory cap.

**Parameters:**

-   `amount` (float): The payment amount.
-   `region` (str): The region where the payment is made.
-   `payment_method` (str, optional): The payment method used. Defaults to "card".

**Returns:**

dict: A dictionary containing the original amount, region, payment method, calculated surcharge (1.5% of amount, rounded to 2 decimals), and the regulatory cap (0.015).

**Example:**

```python
result = calculate_surcharge(amount=100.0, region="US", payment_method="card")
print(result)
# Expected output: {'amount': 100.0, 'region': 'US', 'payment_method': 'card', 'surcharge': 1.5, 'regulatory_cap': 0.015}
```
```
