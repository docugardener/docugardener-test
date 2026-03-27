```markdown
Authorise a card-based payment after validating the payment method.

Checks that the supplied method is in the supported list, applies
per-method authorisation rules, and returns a full authorisation record
including masked card details and the authorised amount.

Raises ValueError for amounts <= 0. Returns a dictionary with `authorised: False` and an `error` key for unsupported payment methods.

Parameters:
    method (str): The payment method (e.g., "visa", "mastercard").
    card_last4 (str): The last four digits of the card number.
    amount (float): The payment amount.

Returns:
    dict: A dictionary containing the authorisation details.  If authorisation is successful, the dictionary will contain the following keys:
        - authorised (bool): True
        - method (str): The payment method.
        - card_last4 (str): The last four digits of the card number.
        - masked (str): The masked card number (e.g., "****1234").
        - amount (float): The payment amount.
        - currency (str): The currency (always "USD").
    If authorisation fails due to an unsupported method, the dictionary will contain:
        - authorised (bool): False
        - error (str): "unsupported_method"
        - method (str): The attempted payment method.

Raises:
    ValueError: If the amount is not positive (<= 0).

Example:
    ```python
    result = payment_5272ee(method="visa", card_last4="1234", amount=100.0)
    print(result)
    # Expected output (if successful):
    # {'authorised': True, 'method': 'visa', 'card_last4': '1234', 'masked': '****1234', 'amount': 100.0, 'currency': 'USD'}

    result = payment_5272ee(method="invalid", card_last4="1234", amount=100.0)
    print(result)
    # Expected output (if unsuccessful):
    # {'authorised': False, 'error': 'unsupported_method', 'method': 'invalid'}

    try:
        payment_5272ee(method="visa", card_last4="1234", amount=-100.0)
    except ValueError as e:
        print(e)
    # Expected output:
    # amount must be positive, got -100.0
    ```
```