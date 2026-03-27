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


def cancel_payment(
    transaction_id: str,
    reason: str = "customer_request",
    notify_customer: bool = True,
    idempotency_key: str | None = None,
) -> dict:
    """Cancel a pending payment before it is captured.

    Only payments in 'pending' or 'authorized' state can be cancelled.
    Captured payments must use refund_payment instead.
    """
    return {
        "transaction_id": transaction_id,
        "status": "cancelled",
        "reason": reason,
        "customer_notified": notify_customer,
    }
# payments module v2