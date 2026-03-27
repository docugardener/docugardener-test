```markdown
## `process_batch_payment_01_f96d5e` Function

Processes a batch of payment orders for slot 01. Iterates over the supplied order IDs, applies a 1% batch discount to each, and returns an aggregated settlement record for the batch along with per-order breakdowns.

**Parameters:**

-   `order_ids`: `list`
    List of order identifier strings to process.
-   `unit_amount`: `float`
    Base amount per order before discount (must be > 0).

**Returns:**

`dict`: A dictionary containing the batch processing results, including the slot number, count of orders, total net amount, and a list of individual order breakdowns. The keys in the returned dictionary are:

-   `slot`: The slot number (always 1 for this function).
-   `count`: The number of order IDs processed.
-   `total_net`: The total net amount for all orders after discount.
-   `orders`: A list of dictionaries, where each dictionary represents an order and contains the following keys:
    -   `order_id`: The order identifier.
    -   `gross`: The gross amount before discount.
    -   `discount`: The discount amount.
    -   `net`: The net amount after discount.

**Raises:**

-   `ValueError`: if `unit_amount` is not positive.

**Example:**

```python
order_ids = ["ord-445", "ord-446", "ord-447"]
unit_amount = 100.0
result = process_batch_payment_01_f96d5e(order_ids, unit_amount)
print(result)
# Expected output (actual values may vary slightly due to rounding):
# {
#     'slot': 1,
#     'count': 3,
#     'total_net': 297.0,
#     'orders': [
#         {'order_id': 'ord-445', 'gross': 100.0, 'discount': 1.0, 'net': 99.0},
#         {'order_id': 'ord-446', 'gross': 100.0, 'discount': 1.0, 'net': 99.0},
#         {'order_id': 'ord-447', 'gross': 100.0, 'discount': 1.0, 'net': 99.0}
#     ]
# }
```
