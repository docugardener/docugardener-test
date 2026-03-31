```markdown
### `process_batch_payment_03_173eba(order_ids: list, unit_amount: float) -> dict`

Process a batch of payment orders for slot 03.

Iterates over the supplied order IDs, applies a 3% batch discount to each, and returns an aggregated settlement record for the batch along with per-order breakdowns.

#### Parameters

*   **`order_ids`** (`list`): List of order identifier strings to process.
*   **`unit_amount`** (`float`): Base amount per order before discount (must be > 0).

#### Returns

*   **`dict`**: A dictionary containing the batch settlement details.
    *   `slot` (`int`): The slot number (always 3).
    *   `count` (`int`): The number of orders processed in the batch.
    *   `total_net` (`float`): The total net amount for all orders after discounts, rounded to two decimal places.
    *   `orders` (`list`): A list of dictionaries, each representing an individual order's breakdown.
        *   `order_id` (`str`): The identifier for the order.
        *   `gross` (`float`): The original `unit_amount` for the order.
        *   `discount` (`float`): The calculated 3% discount for the order, rounded to two decimal places.
        *   `net` (`float`): The net amount for the order after discount, rounded to two decimal places.

#### Raises

*   **`ValueError`**: If `unit_amount` is not positive (i.e., `unit_amount <= 0`).

#### Examples

```python
# Example 1: Process a single order
order_ids_1 = ["ORD-001"]
unit_price_1 = 100.00
result_1 = process_batch_payment_03_173eba(order_ids_1, unit_price_1)
# Expected output:
# {
#     "slot": 3,
#     "count": 1,
#     "total_net": 97.00,
#     "orders": [
#         {"order_id": "ORD-001", "gross": 100.00, "discount": 3.00, "net": 97.00}
#     ]
# }

# Example 2: Process multiple orders with a non-integer unit amount
order_ids_2 = ["ORD-002", "ORD-003"]
unit_price_2 = 50.50
result_2 = process_batch_payment_03_173eba(order_ids_2, unit_price_2)
# Expected output:
# {
#     "slot": 3,
#     "count": 2,
#     "total_net": 97.96,
#     "orders": [
#         {"order_id": "ORD-002", "gross": 50.50, "discount": 1.52, "net": 48.98},
#         {"order_id": "ORD-003", "gross": 50.50, "discount": 1.52, "net": 48.98}
#     ]
# }

# Example 3: Handling invalid unit_amount
try:
    process_batch_payment_03_173eba(["ORD-004"], 0)
except ValueError as e:
    print(e)
# Expected output:
# unit_amount must be positive
```