"""
Errors to be raised in the redditlib module.
"""


__all__ = [
    "AuthFileOpenError"
]


class AuthFileAbsentError(OSError):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __str__(self) -> None:
        return f"Unable to open the specified file as it does not exist: '{self.filename}'"

    
class AuthFileParseError(AuthFileAbsentError):
    def __str__(self) -> None:
        return f"Failed to parse authorization token from file: '{self.filename}'"
