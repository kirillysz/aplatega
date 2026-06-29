from typing import Any, Optional


class APIError(Exception):
    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        endpoint: Optional[str] = None,
        response: Any = None,
        details: Optional[Any] = None,
    ):
        super().__init__(message)

        self.message = message
        self.status_code = status_code
        self.endpoint = endpoint
        self.response = response
        self.details = details

    def __str__(self):
        parts = []

        if self.status_code:
            parts.append(f"HTTP {self.status_code}")

        if self.endpoint:
            parts.append(f"endpoint={self.endpoint}")

        parts.append(self.message)

        return " | ".join(parts)