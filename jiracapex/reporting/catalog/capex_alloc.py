import datetime
import pandas as pd
from jiracapex.reporting.context import ReportContext
from jiracapex.utils.dates import dict_months

# -Ignore / do not count efforts for tickets containing "ARCH", otherwise
# -If Column "Is Support" = Yes, then count task efforts as "Not Classified to CapEx Category", otherwise
# -If Column "Not Classified to CapEx Category" = 1, then count task efforts as "Not Classified to CapEx Category", otherwise
# -If any Column in U to AH =1, then count task efforts in that respective CapEx category, otherwise
# -Count task efforts in the category labeled in Column T
# -Also, report any tasks for which columns T through AI are all empty, or columns U through AI sum to more than 1. 
# -Also, report any tasks for which columns T through AI are all empty (and "Is Support" =NO), 
#   or columns U through AI sum to more than 1. 

def calc_months(df):
    return df.apply(lambda r: dict_months('vv_'
                ,   pd.to_datetime(r.start_date).date()
                ,   pd.to_datetime(r.end_date  ).date()), axis=1)

__rep_config = {
    'query'  : '${project_home}/sql/queries/issue_lifecycle.sql',
    'derive' : [
        {
            'name': 'months',
            'func': calc_months
        }
    ],
    'schema' : {
        'months'     : 'int',
        'duration'   : 'int',
        'start_date' : 'date',
        'end_date'   : 'date',
        'issue_id'   : 'int',
        'issue_key'  : 'str',
    },
    'split' : [
        'months'
    ],
    'column': {'sorted': True},
    'output': '${project_home}/dist/capex_alloc.csv',
    'format': 'csv' 
}

def init_report(context: ReportContext):
    return context.process(__rep_config)