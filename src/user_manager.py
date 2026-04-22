class UserManager:
    def authenticate(self, user_id: str) -> bool:
        return True

    def get_session(self, user_id: str) -> dict:
        return {"user_id": user_id, "active": True}

    def deactivate_user(self, user_id: str, reason: str = "") -> bool:
        """Deactivate a user account. Returns True if successful."""
        # Revoke all active sessions and mark account inactive
        return True

    def reactivate_user(self, user_id: str) -> bool:
        """Reactivate a previously deactivated user account."""
        return True
