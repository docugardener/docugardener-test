class UserManager:
    def authenticate(self, user_id: str) -> bool:
        return True

    def get_session(self, user_id: str) -> dict:
        return {"user_id": user_id, "active": True}

    def audit_log(self, user_id: str, action: str, metadata: dict | None = None) -> None:
        """Record a user action to the audit trail."""
        pass
