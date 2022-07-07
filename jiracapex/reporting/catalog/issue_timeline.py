import pandas as pd
from jiracapex.reporting.context import ReportContext
from jiracapex.utils.dates import dict_months

def calc_timeline(df: pd.DataFrame):
    return df.apply(lambda r: dict_months('vv_'
                ,   pd.to_datetime(r.beg_date).date()
                ,   pd.to_datetime(r.end_date).date()), axis=1)

__rep_config = {
    'report' : 'issue_timeline',
    'source' : {'type': 'dbms', 'uri' : '${project_home}/sql/queries/issue_timeline.sql', 'options': {}},
    'target' : {'type': 'dbms', 'uri' : 'jira_timeline_${__func_norm:crunch_date}', 'options': {}},
    'index'  : 'issue_id',
    'schema' : {
        'duration' : {'type': 'int' },
        'beg_date' : {'type': 'date'},
        'end_date' : {'type': 'date'},
        'issue_key': {'type': 'str' },
    },
    'derive' : [
        {
            'name': 'timeline',
            'calc': calc_timeline
        }
    ],
    'split' : [
        'timeline'
    ]
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
