import pytest
from jiracapex.reporting.tools import load_report, ReportContext

@pytest.fixture
def context() -> ReportContext:
    return ReportContext()

def test_load_report(context: ReportContext):
    rep = load_report('capex_alloc', context)
    assert rep is not None
