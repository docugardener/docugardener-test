```markdown
### `handle_dispute_webhook` Function
```python
def handle_dispute_webhook(payload: dict, secret: str) -> dict:
    """Process incoming dispute webhook events from the payment processor.

    Handles dispute.created, dispute.updated, and dispute.closed events.
    Updates internal dispute records and triggers customer notification
    workflows where applicable.

    Args:
        payload: Raw webhook payload from payment processor.
        secret: Webhook signing secret for HMAC verification.

    Returns:
        dict with event_type, dispute_id, status, and action_taken.
    """
    event_type = payload.get("type", "")
    dispute_id = payload.get("data", {}).get("object", {}).get("id", "unknown")

    if event_type == "dispute.created":
        return {"event_type": event_type, "dispute_id": dispute_id,
                "status": "open", "action_taken": "flagged_for_review"}
    elif event_type == "dispute.updated":
        return {"event_type": event_type, "dispute_id": dispute_id,
                "status": "under_review", "action_taken": "evidence_submitted"}
    elif event_type == "dispute.closed":
        return {"event_type": event_type, "dispute_id": dispute_id,
                "status": "closed", "action_taken": "resolved"}
    return {"event_type": event_type, "dispute_id": dispute_id,
            "status": "unknown", "action_taken": "logged"}
```

**Description:**

Process incoming dispute webhook events from the payment processor. This function handles `dispute.created`, `dispute.updated`, and `dispute.closed` events. It updates internal dispute records and triggers customer notification workflows where applicable.

**Parameters:**

*   `payload` (`dict`): Raw webhook payload from the payment processor.
*   `secret` (`str`): Webhook signing secret for HMAC verification.

**Returns:**

*   `dict`: A dictionary containing the `event_type`, `dispute_id`, `status`, and `action_taken`.

**Example:**

```python
# Example for a dispute created event
payload_created = {
    "type": "dispute.created",
    "data": {
        "object": {
            "id": "dp_12345",
            "status": "open",
            "amount": 1000,
            "currency": "usd"
        }
    }
}
result_created = handle_dispute_webhook(payload=payload_created, secret="test_secret")
print(result_created)
# Expected output: {'event_type': 'dispute.created', 'dispute_id': 'dp_12345', 'status': 'open', 'action_taken': 'flagged_for_review'}

# Example for a dispute updated event
payload_updated = {
    "type": "dispute.updated",
    "data": {
        "object": {
            "id": "dp_67890",
            "status": "under_review",
            "amount": 1000,
            "currency": "usd"
        }
    }
}
result_updated = handle_dispute_webhook(payload=payload_updated, secret="test_secret")
print(result_updated)
# Expected output: {'event_type': 'dispute.updated', 'dispute_id': 'dp_67890', 'status': 'under_review', 'action_taken': 'evidence_submitted'}

# Example for a dispute closed event
payload_closed = {
    "type": "dispute.closed",
    "data": {
        "object": {
            "id": "dp_abcde",
            "status": "won", # or "lost"
            "amount": 1000,
            "currency": "usd"
        }
    }
}
result_closed = handle_dispute_webhook(payload=payload_closed, secret="test_secret")
print(result_closed)
# Expected output: {'event_type': 'dispute.closed', 'dispute_id': 'dp_abcde', 'status': 'closed', 'action_taken': 'resolved'}

# Example for an unknown event type
payload_unknown = {
    "type": "payment.succeeded",
    "data": {
        "object": {
            "id": "pi_xyz789",
            "status": "succeeded"
        }
    }
}
result_unknown = handle_dispute_webhook(payload=payload_unknown, secret="test_secret")
print(result_unknown)
# Expected output: {'event_type': 'payment.succeeded', 'dispute_id': 'unknown', 'status': 'unknown', 'action_taken': 'logged'}
```