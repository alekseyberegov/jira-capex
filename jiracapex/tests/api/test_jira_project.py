import pytest

from jiracapex.api.jira_project import JiraProject

class TestJiraProject:
    def test_query(self, jira_project: JiraProject) -> None:
        resp = jira_project.query()
        assert resp is not None
        assert 'values' in resp