import pandas as pd
from jiracapex.reporting.context import ReportContext
from jiracapex.utils.dates import dict_months

# - Ignore / do not count efforts for tickets containing "ARCH", otherwise
# - If Column "Is Support" = Yes, then count task efforts as "Not Classified to CapEx Category", otherwise
# - If Column "Not Classified to CapEx Category" = 1, then count task efforts as "Not Classified to CapEx Category", otherwise
# - If any Column in U to AH =1, then count task efforts in that respective CapEx category, otherwise
# - Count task efforts in the category labeled in Column T
# - Also, report any tasks for which columns T through AI are all empty, or columns U through AI sum to more than 1. 
# - Also, report any tasks for which columns T through AI are all empty (and "Is Support" =NO), 
#       or columns U through AI sum to more than 1. 

def calc_timeline(df):
    return df.apply(lambda r: dict_months('vv_'
                ,   pd.to_datetime(r.beg_date).date()
                ,   pd.to_datetime(r.end_date).date()), axis=1)

__rep_config = {
    'report' : 'issue_timeline',
    'query'  : '${project_home}/sql/queries/issue_timeline.sql',
    'derive' : [
        {
            'name': 'timeline',
            'calc': calc_timeline
        }
    ],
    'schema' : {
        'timeline' : 'int',
        'duration' : 'int',
        'beg_date' : 'date',
        'end_date' : 'date',
        'issue_id' : 'int',
        'issue_key': 'str',
    },
    'split' : [
        'timeline'
    ],
    'column': {'sort': True},
    'target': {'type': 'dbms', 'output': 'jira_timeline_${__func_norm:crunch_date}', 'options': {}}
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
