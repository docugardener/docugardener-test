```markdown
### `process_batch_payment_02_afd409`

Processes a batch of payment orders for slot 02.

Iterates over the supplied order IDs, applies a 2% batch discount to
each, and returns an aggregated settlement record for the batch along
with per-order breakdowns.

**Parameters:**

*   `order_ids` (list): List of order identifier strings to process.
*   `unit_amount` (float): Base amount per order before discount (must be > 0).

**Returns:**

*   dict: A dictionary containing the slot number (2), the number of orders processed, the total net payment amount, and a list of individual order results. Each order result includes the order ID, gross amount, discount amount, and net amount.

**Example:**

```python
order_ids = ["ord-123", "ord-456", "ord-789"]
unit_amount = 100.0
result = process_batch_payment_02_afd409(order_ids, unit_amount)
print(result)
# Expected output (actual values may vary slightly due to rounding):
# {
#     'slot': 2,
#     'count': 3,
#     'total_net': 294.0,
#     'orders': [
#         {'order_id': 'ord-123', 'gross': 100.0, 'discount': 2.0, 'net': 98.0},
#         {'order_id': 'ord-456', 'gross': 100.0, 'discount': 2.0, 'net': 98.0},
#         {'order_id': 'ord-789', 'gross': 100.0, 'discount': 2.0, 'net': 98.0}
#     ]
# }
```
```