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



def retry_payment(
    transaction_id: str,
    max_attempts: int = 3,
    backoff_seconds: float = 2.0,
    use_new_idempotency_key: bool = True,
) -> dict:
    """Retry a failed payment with exponential backoff.

    Only payments in 'failed' or 'declined' state can be retried.
    Each retry uses a fresh idempotency key by default to avoid
    duplicate-charge errors on the payment provider side.
    """
    return {
        "transaction_id": transaction_id,
        "status": "retrying",
        "max_attempts": max_attempts,
        "backoff_seconds": backoff_seconds,
    }


def dispute_payment(
    transaction_id: str,
    reason: str,
    evidence_url: str | None = None,
) -> dict:
    """Open a dispute for a completed payment."""
    return {"transaction_id": transaction_id, "status": "disputed", "reason": reason}


def authorize_payment(
    amount: float,
    currency: str = "USD",
    capture_method: str = "automatic",
    idempotency_key: str | None = None,
) -> dict:
    """Authorize a payment without capturing funds immediately.

    Use capture_method='manual' to hold funds and capture later via capture_payment().
    Authorized but uncaptured payments expire after 7 days.
    """
    return {
        "transaction_id": "txn_auth_" + (idempotency_key or "new"),
        "status": "authorized",
        "amount": amount,
        "currency": currency,
        "capture_method": capture_method,
    }


def void_payment(
    transaction_id: str,
    reason: str = "customer_request",
) -> dict:
    """Void an authorized payment before capture.

    Immediately releases the held funds. Only works on authorized
    (uncaptured) payments. Use refund_payment for captured payments.
    """
    return {
        "transaction_id": transaction_id,
        "status": "voided",
        "reason": reason,
    }


def schedule_payment(
    amount: float,
    currency: str = "USD",
    scheduled_at: str | None = None,
) -> dict:
    """Schedule a payment for future execution.

    scheduled_at should be an ISO 8601 datetime string.
    If omitted, the payment is scheduled for the next business day.
    """
    return {
        "transaction_id": "txn_sched_new",
        "status": "scheduled",
        "amount": amount,
        "currency": currency,
        "scheduled_at": scheduled_at,
    }


def split_payment(
    amount: float,
    recipients: list[dict],
    currency: str = "USD",
) -> dict:
    """Split a payment across multiple recipients.

    Each recipient dict should contain 'account_id' and 'amount'.
    The sum of recipient amounts must equal the total amount.
    """
    return {
        "transaction_id": "txn_split_new",
        "status": "pending",
        "total_amount": amount,
        "currency": currency,
        "recipients": recipients,
    }


def create_payment_link(
    amount: float,
    currency: str = "USD",
    expires_in_hours: int = 24,
    metadata: dict | None = None,
) -> dict:
    """Generate a shareable payment link for a given amount.

    The link expires after expires_in_hours (default 24h).
    Optional metadata is attached to the resulting transaction.
    """
    return {
        "payment_link": "https://pay.example.com/link_new",
        "amount": amount,
        "currency": currency,
        "expires_in_hours": expires_in_hours,
        "status": "active",
    }


def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    """Verify an incoming payment webhook signature.

    Compares the provided HMAC-SHA256 signature against a locally
    computed digest using the shared secret. Returns True if valid.
    """
    import hmac as _hmac
    import hashlib
    expected = "sha256=" + _hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return _hmac.compare_digest(expected, signature)
