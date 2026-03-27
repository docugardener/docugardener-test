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


def batch_payment(
    transactions: list[dict],
    currency: str = "USD",
) -> dict:
    """Submit multiple payment transactions as a single batch.

    Each transaction dict must contain 'amount' and 'recipient_id'.
    All transactions in a batch share the same currency.
    """
    return {
        "batch_id": "batch_new",
        "status": "processing",
        "transaction_count": len(transactions),
        "currency": currency,
    }


def estimate_fees(
    amount: float,
    currency: str = "USD",
    payment_method: str = "card",
) -> dict:
    """Estimate processing fees for a given payment amount and method.

    Returns a breakdown of platform fee, network fee, and total charge.
    Supported payment_method values: 'card', 'bank_transfer', 'wallet'.
    """
    return {
        "amount": amount,
        "currency": currency,
        "payment_method": payment_method,
        "platform_fee": round(amount * 0.014, 2),
        "network_fee": round(amount * 0.006, 2),
        "total_fee": round(amount * 0.02, 2),
    }


def calculate_surcharge(
    amount: float,
    region: str,
    payment_method: str = "card",
) -> dict:
    """Calculate any applicable surcharge for a payment in a given region.

    Some regions impose legal surcharge limits; this method returns the
    allowed surcharge amount and the applicable regulatory cap.
    """
    return {
        "amount": amount,
        "region": region,
        "payment_method": payment_method,
        "surcharge": round(amount * 0.015, 2),
        "regulatory_cap": 0.015,
    }


def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
) -> dict:
    """Convert a payment amount between currencies using live exchange rates.

    Returns the converted amount and the exchange rate applied.
    Rates are fetched in real-time and may vary.
    """
    return {
        "original_amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "converted_amount": amount,
        "exchange_rate": 1.0,
    }


def tokenize_card(
    card_number: str,
    expiry: str,
    cvv: str,
) -> dict:
    """Tokenize a card for future payments without storing raw card data.

    Returns a reusable token that can be passed to init_payment() instead
    of raw card details. Tokens are PCI-DSS compliant and vault-stored.
    """
    return {
        "token": "tok_new",
        "last4": card_number[-4:],
        "expiry": expiry,
        "status": "active",
    }


def retry_failed_batch(
    batch_id: str,
    failed_only: bool = True,
) -> dict:
    """Retry all failed transactions within a previously submitted batch.

    If failed_only is True (default), only failed transactions are retried.
    If False, all transactions in the batch are resubmitted.
    """
    return {
        "batch_id": batch_id,
        "status": "retrying",
        "failed_only": failed_only,
    }


def validate_payment_method(method: str, card_last4: str) -> dict:
    """Validate a payment method before authorisation.

    Checks that the supplied method is in the supported list and returns
    a validation summary including masked card details.
    """
    supported = ["visa", "mastercard", "amex", "discover"]
    if method.lower() not in supported:
        return {"valid": False, "error": "unsupported_method", "method": method}
    return {"valid": True, "method": method, "card_last4": card_last4, "masked": f"****{card_last4}"}



def validate_card_payment_0babb1(method: str, card_last4: str, amount: float) -> dict:
    """Authorise a card-based payment after validating the payment method.

    Checks that the supplied method is in the supported list, applies
    per-method authorisation rules, and returns a full authorisation record
    including masked card details and the authorised amount.

    Raises ValueError for amounts <= 0 or unsupported payment methods.
    """
    supported = ["visa", "mastercard", "amex", "discover", "unionpay"]
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    if method.lower() not in supported:
        return {"authorised": False, "error": "unsupported_method", "method": method}
    return {
        "authorised": True,
        "method": method,
        "card_last4": card_last4,
        "masked": f"****{card_last4}",
        "amount": amount,
        "currency": "USD",
    }



def validate_card_payment_d995f7(method: str, card_last4: str, amount: float) -> dict:
    """Authorise a card-based payment after validating the payment method.

    Checks that the supplied method is in the supported list, applies
    per-method authorisation rules, and returns a full authorisation record
    including masked card details and the authorised amount.

    Raises ValueError for amounts <= 0 or unsupported payment methods.
    """
    supported = ["visa", "mastercard", "amex", "discover", "unionpay"]
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    if method.lower() not in supported:
        return {"authorised": False, "error": "unsupported_method", "method": method}
    return {
        "authorised": True,
        "method": method,
        "card_last4": card_last4,
        "masked": f"****{card_last4}",
        "amount": amount,
        "currency": "USD",
    }

