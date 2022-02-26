from requests.auth import AuthBase

# https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#authentication

class Endpoint:
    def __init__(self, url: str, auth: AuthBase) -> None:
        self.__url = url
        self.__auth = auth

    @property
    def url(self) -> str:
        return self.__url

    @property
    def auth(self) -> AuthBase:
        return self.__auth