```markdown
### `retry_payment`

```python
def retry_payment(
    transaction_id: str,
    max_attempts: int = 3,
    backoff_seconds: float = 2.0,
    use_new_idempotency_key: bool = True,
) -> dict:
```

Retry a failed payment with exponential backoff.

Only payments in 'failed' or 'declined' state can be retried.
Each retry uses a fresh idempotency key by default to avoid
duplicate-charge errors on the payment provider side.

**Parameters:**

*   `transaction_id` (str): The ID of the failed transaction to retry.
*   `max_attempts` (int): The maximum number of retry attempts. Defaults to 3.
*   `backoff_seconds` (float): The base backoff time in seconds. Defaults to 2.0.
*   `use_new_idempotency_key` (bool): Whether to use a new idempotency key for each retry. Defaults to True.

**Returns:**

*   `dict`: A dictionary containing the transaction ID, status, maximum attempts, and backoff seconds.  The status will be "retrying".

**Example:**

```python
result = retry_payment(transaction_id="txn_123", max_attempts=5, backoff_seconds=3.0)
print(result)
# Expected output: {'transaction_id': 'txn_123', 'status': 'retrying', 'max_attempts': 5, 'backoff_seconds': 3.0}
```

### `dispute_payment`

Adds the `dispute_payment` function to allow users to open disputes for completed payments.

```python
def dispute_payment(transaction_id: str, reason: str, evidence_url: str | None = None) -> dict
```

Opens a dispute for a completed payment.

**Parameters:**

*   `transaction_id` (str): The ID of the transaction to dispute.
*   `reason` (str): The reason for the dispute.
*   `evidence_url` (str, optional): A URL providing evidence for the dispute. Defaults to `None`.

**Returns:**

A dictionary containing the transaction ID and the dispute status.

```python
{
    "transaction_id": transaction_id,
    "status": "disputed",
    "reason": reason
}
```

**Example:**

```python
result = dispute_payment(
    transaction_id="tx123", reason="Fraudulent transaction", evidence_url="http://example.com/evidence"
)
print(result)
# Expected output: {'transaction_id': 'tx123', 'status': 'disputed', 'reason': 'Fraudulent transaction'}
```
```
