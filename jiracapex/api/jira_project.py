from typing import Any
from jiracapex.api.jira_endpoint import Endpoint
import requests
import json

# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-search-get

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