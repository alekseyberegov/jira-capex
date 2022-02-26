from typing import Any
from jiracapex.api.jira_endpoint import Endpoint
import requests
import json

class JiraProject:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"}

    def __init__(self, endpoint:  Endpoint) -> None:
        self.__endpoint = endpoint

    def query(self) -> Any:
        response = requests.request(
            "GET",
            self.__endpoint.url,
            headers=JiraProject.headers,
            auth=self.__endpoint.auth)

        return json.loads(response.text)