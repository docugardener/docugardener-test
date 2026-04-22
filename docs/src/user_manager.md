```markdown
### User Management
The `UserManager` class handles user authentication and session lifecycle.
It is an internal implementation detail and not exposed as a public API.

#### `authenticate(user_id: str) -> bool`
Authenticates a user.

*   **Parameters:**
    *   `user_id` (str): The ID of the user to authenticate.
*   **Returns:**
    *   `bool`: `True` if authentication is successful, `False` otherwise.

#### `get_session(user_id: str) -> dict`
Retrieves the session information for a given user.

*   **Parameters:**
    *   `user_id` (str): The ID of the user whose session to retrieve.
*   **Returns:**
    *   `dict`: A dictionary containing session details, including `user_id` and `active` status.

#### `deactivate_user(user_id: str, reason: str = "") -> bool`
Deactivates a user account.

*   **Parameters:**
    *   `user_id` (str): The ID of the user to deactivate.
    *   `reason` (str, optional): The reason for deactivation. Defaults to "".
*   **Returns:**
    *   `bool`: `True` if the deactivation was successful.

#### `reactivate_user(user_id: str) -> bool`
Reactivates a previously deactivated user account.

*   **Parameters:**
    *   `user_id` (str): The ID of the user to reactivate.
*   **Returns:**
    *   `bool`: `True` if the reactivation was successful.
```