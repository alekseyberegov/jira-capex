import pytest

from configparser import ConfigParser
from requests import auth

from jiracapex.api.jira_search import JiraSearch
from jiracapex.conf.config_loader import ConfigLoader

@pytest.fixture
def config() -> ConfigParser:
    loader: ConfigLoader = ConfigLoader("jiracapex.ini")
    return loader.config()

@pytest.fixture(scope="function")
def jira_search(config: ConfigParser) -> JiraSearch:
    credentials = auth.HTTPBasicAuth(config.get('auth', 'user'), config.get('auth', 'token'))
    search: JiraSearch = JiraSearch(config.get('jira', 'search_url'), credentials)
    return search

class TestJiraSearch:
    def test_single_issue(self, jira_search: JiraSearch):
        jira_search.set_fields(["summary", "status", "assignee", "created", "creator"])
        resp = jira_search.query("project=OL")
        assert resp is not None
        assert 'issues' in resp