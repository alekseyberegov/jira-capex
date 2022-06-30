import pytest
from jiracapex.reporting.runner import ReportRunner
from jiracapex.reporting.context import ReportContext
from sqlalchemy import create_engine

@pytest.fixture
def context() -> ReportContext:
    context = ReportContext()
    context.set_var('project_home', 'alex')
    return context

@pytest.fixture
def engine():
    return create_engine('sqlite:///:memory:', echo = True)

@pytest.fixture
def runner(engine) -> ReportRunner:
    runner = ReportRunner(engine)
    return runner

def test_get_report(context: ReportContext, runner: ReportRunner):
    rep = runner.get_report('capex_alloc', context)
    assert rep is not None
    assert rep['query'] == 'alex/sql/queries/issue_lifecycle.sql'
