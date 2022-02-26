import pytest
from configparser import ConfigParser
from requests import auth
from jiracapex.conf.config_loader import ConfigLoader
from jiracapex.api.jira_endpoint import Endpoint
from jiracapex.api.jira_search import JiraSearch
from jiracapex.api.jira_project import JiraProject

@pytest.fixture
def config() -> ConfigParser:
    loader: ConfigLoader = ConfigLoader("jiracapex.ini")
    return loader.config()

def endpoint(config, name) -> Endpoint:
   return Endpoint(config.get('jira', name), 
        auth.HTTPBasicAuth(config.get('auth', 'user'), config.get('auth', 'token')))

@pytest.fixture(scope="function")
def jira_search(config) -> JiraSearch:
    search: JiraSearch = JiraSearch(endpoint(config, 'search_url'))
    return search

@pytest.fixture(scope="function")
def jira_project(config) -> JiraProject:
    project: JiraProject = JiraProject(endpoint(config, 'project_url'))
    return project
