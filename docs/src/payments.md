```markdown
## dispute_payment

Open or respond to a payment dispute (chargeback).

Submits dispute evidence to the payment processor. Evidence should
include customer communications, shipping proof, and service records.
Disputes not responded to within 7 days are automatically lost.

### Parameters

*   `transaction_id` (str): The disputed payment's transaction ID.
*   `reason` (str): Dispute reason code (e.g. 'fraudulent', 'product_not_received').
*   `evidence` (dict | None, optional): Dict of supporting documents. Keys: customer_communication, shipping_documentation, service_documentation. Defaults to None.
*   `submit_immediately` (bool, optional): If True, submits evidence to processor right away. If False, saves as draft for review. Defaults to False.

### Returns

*   dict: A dictionary containing the dispute details with the following keys:
    *   `transaction_id` (str): The ID of the transaction being disputed.
    *   `dispute_id` (str): A unique identifier for the dispute.
    *   `reason` (str): The reason code for the dispute.
    *   `status` (str): The status of the dispute ('draft' or 'submitted').
    *   `evidence_received` (bool): True if evidence was provided, False otherwise.
    *   `deadline_days` (int): The number of days until the dispute is automatically lost if not responded to.

### Example

```python
# Open a dispute and save as draft
dispute_draft = dispute_payment(
    transaction_id="txn_12345",
    reason="product_not_received"
)
print(dispute_draft)
# Output: {'transaction_id': 'txn_12345', 'dispute_id': 'dp_txn_12345', 'reason': 'product_not_received', 'status': 'draft', 'evidence_received': False, 'deadline_days': 7}

# Open a dispute and submit evidence immediately
dispute_submitted = dispute_payment(
    transaction_id="txn_67890",
    reason="fraudulent",
    evidence={
        "customer_communication": "email_log.txt",
        "shipping_documentation": "tracking_info.pdf"
    },
    submit_immediately=True
)
print(dispute_submitted)
# Output: {'transaction_id': 'txn_67890', 'dispute_id': 'dp_txn_67890', 'reason': 'fraudulent', 'status': 'submitted', 'evidence_received': True, 'deadline_days': 7}
```
```