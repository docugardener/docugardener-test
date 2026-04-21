```markdown
### `process_batch_payment_03_af9a47`
Processes a batch of payment orders for slot 03.

Iterates over the supplied order IDs, applies a 3% batch discount to
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
order_ids = ["ord-123", "ord-456"]
unit_amount = 100.0
result = process_batch_payment_03_af9a47(order_ids, unit_amount)
print(result)
# Expected output:
# {'slot': 3, 'count': 2, 'total_net': 194.0, 'orders': [{'order_id': 'ord-123', 'gross': 100.0, 'discount': 3.0, 'net': 97.0}, {'order_id': 'ord-456', 'gross': 100.0, 'discount': 3.0, 'net': 97.0}]}
```
```