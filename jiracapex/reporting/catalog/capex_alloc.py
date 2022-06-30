from jiracapex.reporting.context import ReportContext

# -Ignore / do not count efforts for tickets containing "ARCH", otherwise
# -If Column "Is Support" = Yes, then count task efforts as "Not Classified to CapEx Category", otherwise
# -If Column "Not Classified to CapEx Category" = 1, then count task efforts as "Not Classified to CapEx Category", otherwise
# -If any Column in U to AH =1, then count task efforts in that respective CapEx category, otherwise
# -Count task efforts in the category labeled in Column T
# -Also, report any tasks for which columns T through AI are all empty, or columns U through AI sum to more than 1. 
# -Also, report any tasks for which columns T through AI are all empty (and "Is Support" =NO), 
#   or columns U through AI sum to more than 1. 

__rep_config = {
    'query'  : '${project_home}/sql/queries/issue_lifecycle.sql',
    'derive' : [
        {
            'name': 'months',
            'func': lambda df: df.duration // 30
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
    'output': '${project_home}/dist/capex_alloc.csv',
    'format': 'csv' 
}

def init_report(context: ReportContext):
    return context.process(__rep_config)