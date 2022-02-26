import pytest
from jiracapex.api.jira_search import JiraSearch

class TestJiraSearch:
    def test_single_issue(self, jira_search: JiraSearch):
        jira_search.set_fields(["summary", "status", "assignee", "created", "creator"])
        resp = jira_search.query("project=OL")
        assert resp is not None
        assert 'issues' in resp