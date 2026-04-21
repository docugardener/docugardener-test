```markdown
### `process_batch_payment_04_5988bf`
```python
def process_batch_payment_04_5988bf(order_ids: list, unit_amount: float) -> dict:
```

Processes a batch of payment orders for slot 04.

This function iterates over the supplied order IDs, applies a 4% batch discount to each order, and returns an aggregated settlement record for the batch along with per-order breakdowns.

**Parameters:**

*   **`order_ids`** (`list`): A list of order identifier strings to process.
*   **`unit_amount`** (`float`): The base amount per order before the discount is applied. This value must be positive.

**Returns:**

*   **`dict`**: A dictionary containing the aggregated settlement record and individual order details.
    *   `slot` (`int`): The slot number (always 4).
    *   `count` (`int`): The total number of orders processed in the batch.
    *   `total_net` (`float`): The sum of net amounts for all orders after discounts.
    *   `orders` (`list`): A list of dictionaries, each representing an individual order's breakdown:
        *   `order_id` (`str`): The identifier of the order.
        *   `gross` (`float`): The original amount of the order before discount.
        *   `discount` (`float`): The calculated discount amount for the order.
        *   `net` (`float`): The final amount after the discount is applied.

**Raises:**

*   **`ValueError`**: If `unit_amount` is not positive.

**Examples:**

```python
>>> process_batch_payment_04_5988bf(["ord-abc", "ord-def"], 100.0)
{'slot': 4, 'count': 2, 'total_net': 192.0, 'orders': [{'order_id': 'ord-abc', 'gross': 100.0, 'discount': 4.0, 'net': 96.0}, {'order_id': 'ord-def', 'gross': 100.0, 'discount': 4.0, 'net': 96.0}]}
```
```