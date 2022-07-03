import pytest
from jiracapex.reporting.runner import ReportRunner, Report
from jiracapex.reporting.context import ReportContext
from sqlalchemy import create_engine

@pytest.fixture
def context() -> ReportContext:
    context = ReportContext()
    context['project_home'] = 'jira-capex'
    context['crunch_date' ] = '2020-06-06'
    return context

@pytest.fixture
def engine():
    return create_engine('sqlite:///:memory:', echo = True)

@pytest.fixture
def runner(engine) -> ReportRunner:
    runner = ReportRunner(engine)
    return runner

def test_get_report(context: ReportContext, runner: ReportRunner):
    rpt = runner.get_report('issue_timeline', context)
    assert rpt is not None
    assert rpt['query'] == 'jira-capex/sql/queries/issue_timeline.sql'
