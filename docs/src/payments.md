```markdown
Adds the `dispute_payment` function to allow users to open disputes for completed payments.

### dispute_payment

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