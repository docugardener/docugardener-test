```markdown
### `process_batch_payment_04_e25d25`

```python
process_batch_payment_04_e25d25(order_ids: list, unit_amount: float) -> dict
```

Process a batch of payment orders for slot 04.

This function iterates over the supplied order IDs, applies a 4% batch discount to each, and returns an aggregated settlement record for the batch along with per-order breakdowns.

**Parameters:**

*   `order_ids` (`list`): A list of order identifier strings to process.
*   `unit_amount` (`float`): The base amount per order before discount. This value must be positive.

**Returns:**

*   `dict`: A dictionary containing the aggregated settlement record and per-order breakdowns.
    *   `slot` (`int`): The slot number (always 4).
    *   `count` (`int`): The number of orders processed.
    *   `total_net` (`float`): The sum of net amounts for all orders in the batch, rounded to two decimal places.
    *   `orders` (`list`): A list of dictionaries, each representing an individual order's breakdown.
        *   `order_id` (`str`): The identifier for the order.
        *   `gross` (`float`): The original `unit_amount` for the order.
        *   `discount` (`float`): The calculated 4% discount for the order, rounded to two decimal places.
        *   `net` (`float`): The net amount for the order after discount, rounded to two decimal places.

**Raises:**

*   `ValueError`: If `unit_amount` is not positive.

**Example:**

```python
from src.batch_04_e25d25 import process_batch_payment_04_e25d25

# Process a batch of orders
order_ids = ["order_A1", "order_B2", "order_C3"]
unit_amount = 100.00
result = process_batch_payment_04_e25d25(order_ids, unit_amount)
print(result)
# Expected output:
# {
#     'slot': 4,
#     'count': 3,
#     'total_net': 288.0,
#     'orders': [
#         {'order_id': 'order_A1', 'gross': 100.0, 'discount': 4.0, 'net': 96.0},
#         {'order_id': 'order_B2', 'gross': 100.0, 'discount': 4.0, 'net': 96.0},
#         {'order_id': 'order_C3', 'gross': 100.0, 'discount': 4.0, 'net': 96.0}
#     ]
# }

# Example with a different unit amount
order_ids_2 = ["order_X", "order_Y"]
unit_amount_2 = 50.50
result_2 = process_batch_payment_04_e25d25(order_ids_2, unit_amount_2)
print(result_2)
# Expected output:
# {
#     'slot': 4,
#     'count': 2,
#     'total_net': 96.96,
#     'orders': [
#         {'order_id': 'order_X', 'gross': 50.5, 'discount': 2.02, 'net': 48.48},
#         {'order_id': 'order_Y', 'gross': 50.5, 'discount': 2.02, 'net': 48.48}
#     ]
# }
```
```