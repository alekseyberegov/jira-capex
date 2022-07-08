import pandas as pd
from jiracapex.reporting.context import ReportContext
from jiracapex.utils.dates import dict_months

def calc_timeline(x):
    beg = pd.to_datetime(x.beg_date).date()
    end = pd.to_datetime(x.end_date).date()
    return dict_months('vv_', beg, end)

__rep_config = {
    'report' : 'issue_timeline',
    'source' : {'type': 'dbms', 'uri' : '${project_home}/sql/queries/issue_timeline.sql', 'options': {}},
    'target' : {'type': 'dbms', 'uri' : 'jira_timeline_${__func_norm:crunch_date}', 'options': {}},
    'schema' : {
        'issue_id' : {'type': 'int' },
        'issue_key': {'type': 'str' },
        'duration' : {'type': 'int' },
        'beg_date' : {'type': 'date'},
        'end_date' : {'type': 'date'},
    },
    'derive' : [
        {
            'name': 'tmjson',
            'calc': calc_timeline
        }
    ],
    'split' : [
        'tmjson'
    ],
    'index'  : 'issue_id'
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
