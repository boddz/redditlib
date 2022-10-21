from urllib import request, parse
from os import path
from sys import version_info

from .errors import AuthFileAbsentError, AuthFileParseError


class HeaderUtils:
        
    @staticmethod
    def user_agent() -> str:
        """
        Return a generic user agent for the module.
        """
        py = f"Python {version_info[0]}.{version_info[1]}.{version_info[2]}"
        return f"Redditlib (Bot) {py}"

    @staticmethod
    def auth_file(filepath: str = "./auth.txt") -> str:
        """
        Open file and parse the authorization token to use in headers.
        """
        filepath = str(filepath)
        
        if path.exists(filepath) is False:
            raise AuthFileAbsentError(str(filepath))

        try:
            with open(filepath, "r") as authfile:
                return authfile.read().strip()
        except AuthFileParseError:
            raise AuthFileParseError(filepath)

        
class Posting:

    def __init__(self,
                 auth: str,  # The authorization token to use in headers.
                 user_agent: str  # The user agent to send in header.
                 ) -> None:

        self.auth = auth
        self.user_agent = user_agent
    
    _API = "https://oauth.reddit.com/api"
    _PARAMS = "submit?resubmit=true&redditWebClient=desktop2x&app=desktop2x-client-production&rtj=only&raw_json=1&gilding_detail=1"
    _URL = f"{_API}/{_PARAMS}"

    def upload_post(self, content: str) -> None:
        req = request.Request(
            url=self._URL,
            data=content.encode("utf-8"),
            headers={"Authorization": self.auth, "User-Agent": self.user_agent, "Content-Type": "application/x-www-form-urlencoded"})
        with request.urlopen(req) as req:
            print(req.status)
