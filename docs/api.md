# Payment API

## Endpoints

### POST /payments/init

Initiates a payment transaction.

**Parameters:**
- `amount` (float, required) — payment amount in the account's default currency

**Response:**
```json
{ "transaction_id": "txn_123", "status": "pending" }
```
