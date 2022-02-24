from typing import array, Any
from requests.auth import AuthBase
import requests
import json

class JiraProject:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"}

    def __init__(self, endpoint: str, auth: AuthBase) -> None:
        self.__endpoint = endpoint
        self.__auth = auth

    def query(self) -> Any:
        response = requests.request(
            "GET",
            self.__endpoint,
            headers=JiraProject.headers,
            auth=self.__auth)

        return json.loads(response.text)