```markdown
Adds the `retry_failed_batch` function to retry transactions in a batch.

### `retry_failed_batch`

Retries transactions from a previously submitted batch.  By default, only failed transactions are retried.

```python
def retry_failed_batch(batch_id: str, failed_only: bool = True) -> dict
```

**Parameters:**

*   `batch_id` (str): The ID of the batch to retry.
*   `failed_only` (bool, optional): If `True` (default), only failed transactions are retried. If `False`, all transactions in the batch are resubmitted.

**Returns:**

*   `dict`: A dictionary containing the `batch_id`, a status of `"retrying"`, and the `failed_only` flag.

**Example:**

```python
result = retry_failed_batch(batch_id="batch123", failed_only=False)
print(result)
# Expected output: {'batch_id': 'batch123', 'status': 'retrying', 'failed_only': False}
```
```