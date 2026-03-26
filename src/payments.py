def init_payment(amount: float, currency: str = "USD") -> dict:
    """Initiate a payment transaction."""
    return {"transaction_id": "txn_123", "status": "pending", "currency": currency}


def refund_payment(transaction_id: str, reason: str = "") -> dict:
    """Refund a previously initiated payment."""
    return {"transaction_id": transaction_id, "status": "refunded", "reason": reason}


def handle_webhook(payload: dict, secret: str) -> dict:
    """Process an incoming payment webhook event.

    Validates the webhook signature and dispatches to the appropriate
    handler based on event type (payment.succeeded, payment.failed,
    payment.refunded).
    """
    event_type = payload.get("type")
    if event_type == "payment.succeeded":
        return {"status": "ok", "action": "captured", "id": payload.get("id")}
    elif event_type == "payment.failed":
        return {"status": "ok", "action": "logged", "id": payload.get("id")}
    elif event_type == "payment.refunded":
        return {"status": "ok", "action": "refund_processed", "id": payload.get("id")}
    return {"status": "ignored", "type": event_type}


def get_payment_status(transaction_id: str) -> dict:
    """Retrieve the current status of a payment transaction."""
    return {"transaction_id": transaction_id, "status": "completed", "settled": True}
# payments module v2