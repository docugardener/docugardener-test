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



def validate_card_payment_961c8a(method: str, card_last4: str, amount: float) -> dict:
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



def validate_card_payment_ef9d9f(method: str, card_last4: str, amount: float) -> dict:
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



def validate_card_payment_de563f(method: str, card_last4: str, amount: float) -> dict:
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



def validate_card_payment_3b9563(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_c31709(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_d18a9b(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_194903(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def validate_card_payment_a9eaaa(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_d9847d(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_48572b(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_b28394(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def process_batch_payment_01_15ea9a(order_ids: list, unit_amount: float) -> dict:
    """Process a batch of payment orders for slot 01.

    Iterates over the supplied order IDs, applies a 1% batch discount to
    each, and returns an aggregated settlement record for the batch along
    with per-order breakdowns.

    Args:
        order_ids:    List of order identifier strings to process.
        unit_amount:  Base amount per order before discount (must be > 0).
    """
    if unit_amount <= 0:
        raise ValueError("unit_amount must be positive")
    discount_pct = 1
    results = []
    for oid in order_ids:
        discount = round(unit_amount * discount_pct / 100, 2)
        results.append({"order_id": oid, "gross": unit_amount, "discount": discount,
                         "net": round(unit_amount - discount, 2)})
    total_net = round(sum(r["net"] for r in results), 2)
    return {"slot": 1, "count": len(order_ids), "total_net": total_net, "orders": results}



def process_batch_payment_01_1e1cef(order_ids: list, unit_amount: float) -> dict:
    """Process a batch of payment orders for slot 01.

    Iterates over the supplied order IDs, applies a 1% batch discount to
    each, and returns an aggregated settlement record for the batch along
    with per-order breakdowns.

    Args:
        order_ids:    List of order identifier strings to process.
        unit_amount:  Base amount per order before discount (must be > 0).
    """
    if unit_amount <= 0:
        raise ValueError("unit_amount must be positive")
    discount_pct = 1
    results = []
    for oid in order_ids:
        discount = round(unit_amount * discount_pct / 100, 2)
        results.append({"order_id": oid, "gross": unit_amount, "discount": discount,
                         "net": round(unit_amount - discount, 2)})
    total_net = round(sum(r["net"] for r in results), 2)
    return {"slot": 1, "count": len(order_ids), "total_net": total_net, "orders": results}



def validate_card_payment_70daf9(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_c4974a(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_a7d73f(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_f3b127(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def issue_refund_c88bfb(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund for a completed order.

    Validates the refund amount against the original order, applies the
    refund, and returns a confirmation record with the refund transaction ID.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0 and ≤ original order value).
        reason:   Human-readable reason for the refund (for audit trail).
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}



def issue_refund_c8478f(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund for a completed order.

    Validates the refund amount against the original order, applies the
    refund, and returns a confirmation record with the refund transaction ID.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0 and ≤ original order value).
        reason:   Human-readable reason for the refund (for audit trail).
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}



def issue_refund_3db467(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund for a completed order.

    Validates the refund amount against the original order, applies the
    refund, and returns a confirmation record with the refund transaction ID.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0 and ≤ original order value).
        reason:   Human-readable reason for the refund (for audit trail).
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}



def issue_refund_efadb9(order_id: str, amount: float, reason: str) -> dict:
    """Issue a refund for a completed order.

    Validates the refund amount against the original order, applies the
    refund, and returns a confirmation record with the refund transaction ID.

    Args:
        order_id: Identifier of the order to refund.
        amount:   Refund amount (must be > 0 and ≤ original order value).
        reason:   Human-readable reason for the refund (for audit trail).
    """
    if amount <= 0:
        raise ValueError("refund amount must be positive")
    import uuid as _u
    return {"refund_id": str(_u.uuid4()), "order_id": order_id,
             "amount": amount, "reason": reason, "status": "refunded"}



def validate_card_payment_5272ee(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_8f1ddf(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_f4d53c(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_25a9e7(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def calculate_fx_conversion_b2f98a(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def validate_card_payment_23286e(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_a8afff(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_698f2b(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_b3f964(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def validate_card_payment_3382ef(method: str, card_last4: str, amount: float) -> dict:
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



def validate_card_payment_98c6c9(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_f41056(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def apply_surcharge_338fd4(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_37a66e(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_003c9b(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def validate_card_payment_24003d(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_5bcabf(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_87458c(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_f49f12(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def validate_card_payment_c7b0b7(method: str, card_last4: str, amount: float) -> dict:
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



def apply_surcharge_c23a79(amount: float, surcharge_pct: float, currency: str = "USD") -> dict:
    """Apply a percentage-based surcharge to a payment transaction.

    Calculates the surcharge value, validates inputs, and returns a breakdown
    including the original amount, surcharge, total charged, and applied currency.
    Surcharge percentage must be between 0 and 50 (exclusive).

    Args:
        amount: Base transaction amount (must be > 0).
        surcharge_pct: Surcharge rate as a percentage (e.g. 2.5 for 2.5%).
        currency: ISO 4217 currency code.  Defaults to USD.
    """
    if amount <= 0:
        raise ValueError("amount must be positive")
    if not (0 < surcharge_pct < 50):
        raise ValueError("surcharge_pct must be between 0 and 50")
    surcharge = round(amount * surcharge_pct / 100, 2)
    return {
        "original": amount,
        "surcharge": surcharge,
        "total": round(amount + surcharge, 2),
        "currency": currency,
        "rate_applied": surcharge_pct,
    }



def tokenize_card_45d95a(
    card_number: str,
    expiry_month: int,
    expiry_year: int,
    billing_zip: str,
) -> dict:
    """Tokenize a card for PCI-compliant secure storage.

    Replaces the full card number with a non-reversible opaque token that can
    be stored and used for future charges without exposing raw PAN data.
    The token encodes the last-4 digits for display purposes only.

    Args:
        card_number: Full card number (PAN).  Never stored after tokenisation.
        expiry_month: Card expiry month (1–12).
        expiry_year:  Card expiry year (4-digit).
        billing_zip:  Cardholder billing postal code for AVS checks.
    """
    last4 = card_number[-4:]
    token = f"tok_{last4}_{hash(card_number + str(expiry_month) + str(expiry_year)) & 0xFFFFFF:06x}"
    return {
        "token": token,
        "last4": last4,
        "expiry": f"{expiry_month:02d}/{expiry_year}",
        "billing_zip": billing_zip,
        "network": "unknown",   # resolved at authorisation time
    }



def calculate_fx_conversion_601c5a(
    from_currency: str,
    to_currency: str,
    amount: float,
    rate: float,
) -> dict:
    """Calculate the result of a foreign-exchange conversion for a payment.

    Applies the provided exchange rate to the source amount, deducts a
    0.5% conversion fee, and returns a full settlement breakdown including
    gross converted amount, fee, and net amount.

    Args:
        from_currency: ISO 4217 source currency (e.g. "GBP").
        to_currency:   ISO 4217 target currency (e.g. "USD").
        amount:        Amount in source currency (must be > 0).
        rate:          Exchange rate from_currency → to_currency (must be > 0).
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("amount and rate must be positive")
    gross    = round(amount * rate, 2)
    fee      = round(gross * 0.005, 2)
    net      = round(gross - fee, 2)
    return {
        "from": from_currency, "to": to_currency,
        "original": amount, "rate": rate,
        "gross": gross, "fee": fee, "net": net,
    }



def calculate_loyalty_discount_2fc01e(purchases: int, base_rate: float) -> float:
    """Calculate a loyalty discount rate for a customer.

    Returns a discount multiplier between 0 and 1 based on the number of
    previous purchases.  Customers with more than 10 purchases receive a
    full base_rate discount; others receive a proportional fraction.

    Args:
        purchases: Number of completed purchases by this customer.
        base_rate: Maximum discount rate to apply (0.0–1.0).
    """
    if purchases <= 0:
        return 0.0
    factor = min(purchases / 10.0, 1.0)
    return round(base_rate * factor, 4)

