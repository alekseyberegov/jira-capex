from typing import Any
from jiracapex.api.jira_endpoint import Endpoint
from jiracapex.url.utils import url_add_params
import requests
import json

# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-changelog-get

class JiraChangelog:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def __init__(self, endpoint: Endpoint) -> None:
        self.__endpoint = endpoint

    def query(self, issue_id: str, start_at: int = 0, max_results: int = 1) -> Any:
        response = requests.request(
            "GET",
            url_add_params(self.__endpoint.url.format(id=issue_id), {'startAt': start_at, 'maxResults': max_results}),
            headers=JiraChangelog.headers,
            auth=self.__endpoint.auth)

        return json.loads(response.text)