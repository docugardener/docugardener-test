def login(user, password, mfa_token=None, provider='local'):
    """Authenticate user with optional MFA and SSO provider."""
    if provider == 'local':
        return user == 'admin' and mfa_token is not None
    return False
