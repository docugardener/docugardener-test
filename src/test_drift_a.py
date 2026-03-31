def validate_email(email):
    if not email or '@' not in email:
        return False
    parts = email.split('@')
    return len(parts) == 2 and '.' in parts[1]
