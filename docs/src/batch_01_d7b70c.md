```markdown
### `process_batch_payment_01_d7b70c`
Processes a batch of payment orders for slot 01.

Iterates over the supplied order IDs, applies a 1% batch discount to
each, and returns an aggregated settlement record for the batch along
with per-order breakdowns.

**Parameters:**

*   `order_ids` (list): List of order identifier strings to process.
*   `unit_amount` (float): Base amount per order before discount (must be > 0).

**Returns:**

*   `dict`: A dictionary containing the settlement record for the batch, including the slot number, count of orders, total net amount, and a list of per-order breakdowns.

**Raises:**

*   `ValueError`: If `unit_amount` is not positive.

**Example:**

```python
order_ids = ["ord-abc", "ord-def"]
unit_amount = 50.0
result = process_batch_payment_01_d7b70c(order_ids, unit_amount)
print(result)
# Expected output:
# {'slot': 1, 'count': 2, 'total_net': 99.0, 'orders': [{'order_id': 'ord-abc', 'gross': 50.0, 'discount': 0.5, 'net': 49.5}, {'order_id': 'ord-def', 'gross': 50.0, 'discount': 0.5, 'net': 49.5}]}
```
```