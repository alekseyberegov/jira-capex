from array import array
from typing import Any
from jiracapex.api.jira_endpoint import Endpoint
import requests
import json

# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-post

class JiraSearch:
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  def __init__(self, endpoint: Endpoint) -> None:
      self.__endpoint = endpoint
      self.__expand = []

  def set_expand(self, expand: array) -> None:
      self.__expand = expand

  def set_fields(self, fields: array) -> None:
    self.__fields = fields

  def query(self, jql: str, start_at: int = 0, max_results: int = 1) -> Any:
    payload = {
      "expand": self.__expand,
      "jql": jql,
      "maxResults": max_results,
      "fieldsByKeys": False,
      "fields": self.__fields,
      "startAt": start_at
    }

    assert self.__endpoint is not None

    response = requests.request(
      "POST",
      self.__endpoint.url,
      data = json.dumps(payload),
      headers = JiraSearch.headers,
      auth = self.__endpoint.auth)

    return json.loads(response.text)