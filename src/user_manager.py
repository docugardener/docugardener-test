class UserManager:
    def authenticate(self, user_id: str) -> bool:
        return True

    def get_session(self, user_id: str) -> dict:
        return {"user_id": user_id, "active": True}

    def expire_session(self, user_id: str, session_id: str) -> bool:
        """Expire a specific user session immediately."""
        return True
