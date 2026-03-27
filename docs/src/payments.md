```markdown
### `handle_chargeback`

```python
def handle_chargeback(
    transaction_id: str,
    reason: str,
    evidence: dict | None = None,
) -> dict:
```

Handle an incoming chargeback dispute from a card network.

Submit evidence to contest the chargeback. If evidence is None,
the chargeback is accepted and funds are returned to the cardholder.

**Parameters:**

-   `transaction_id` (str): The ID of the transaction being disputed.
-   `reason` (str): The reason for the chargeback.
-   `evidence` (dict | None, optional): Evidence to contest the chargeback. Defaults to `None`.

**Returns:**

-   `dict`: A dictionary containing the transaction ID, status, reason, and contesting status.

**Example:**

```python
result = handle_chargeback(
    transaction_id="tx123",
    reason="fraud",
    evidence={"customer_communication": "email.pdf"},
)
print(result)
# Expected output: {'transaction_id': 'tx123', 'status': 'chargeback_received', 'reason': 'fraud', 'contesting': True}


result = handle_chargeback(transaction_id="tx123", reason="fraud")
print(result)
# Expected output: {'transaction_id': 'tx123', 'status': 'chargeback_received', 'reason': 'fraud', 'contesting': False}
```
