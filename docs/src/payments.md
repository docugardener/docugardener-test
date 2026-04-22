```markdown
## schedule_payment

Schedule a payment to be executed at a future time.

This function schedules a payment for a future execution. It supports an optional `customer_id` and `scheduled_at` timestamp. If `scheduled_at` is not provided, the payment is scheduled for immediate execution. The function also includes a `retry_on_failure` parameter to enable automatic retries with exponential backoff in case of initial failure.

### Parameters

*   `amount` (float): The amount to be paid.
*   `currency` (str, optional): The currency of the payment. Defaults to "USD".
*   `customer_id` (str | None, optional): The ID of the customer for whom the payment is scheduled. Defaults to None.
*   `scheduled_at` (str | None, optional): The ISO 8601 datetime string when the payment should be scheduled. If omitted, the payment is scheduled for immediate execution. Defaults to None.
*   `retry_on_failure` (bool, optional): Whether to automatically retry the payment on failure. Defaults to True.

### Returns

*   `dict`: A dictionary containing the `schedule_id`, `status`, `amount`, `currency`, `customer_id`, `scheduled_at`, and `retry_on_failure` of the scheduled payment.

### Example

```python
# Schedule a payment for a specific customer at a future date with retries enabled
payment_schedule = schedule_payment(
    amount=100.00,
    currency="EUR",
    customer_id="cust_123",
    scheduled_at="2024-12-31T23:59:59Z",
    retry_on_failure=True
)
print(payment_schedule)
# Expected output: {'schedule_id': 'sched_abc123', 'status': 'scheduled', 'amount': 100.0, 'currency': 'EUR', 'customer_id': 'cust_123', 'scheduled_at': '2024-12-31T23:59:59Z', 'retry_on_failure': True}

# Schedule a payment for immediate execution without retries
payment_schedule_immediate = schedule_payment(
    amount=50.00,
    retry_on_failure=False
)
print(payment_schedule_immediate)
# Expected output: {'schedule_id': 'sched_abc123', 'status': 'scheduled', 'amount': 50.0, 'currency': 'USD', 'customer_id': None, 'scheduled_at': None, 'retry_on_failure': False}
```
```