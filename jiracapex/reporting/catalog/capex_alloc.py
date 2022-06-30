from jiracapex.reporting.tools import ReportContext

# -Ignore / do not count efforts for tickets containing "ARCH", otherwise
# -If Column "Is Support" = Yes, then count task efforts as "Not Classified to CapEx Category", otherwise
# -If Column "Not Classified to CapEx Category" = 1, then count task efforts as "Not Classified to CapEx Category", otherwise
# -If any Column in U to AH =1, then count task efforts in that respective CapEx category, otherwise
# -Count task efforts in the category labeled in Column T
# -Also, report any tasks for which columns T through AI are all empty, or columns U through AI sum to more than 1. 
# -Also, report any tasks for which columns T through AI are all empty (and "Is Support" =NO), 
#   or columns U through AI sum to more than 1. 

__rep_config = {
    'name'  : 'capex_alloc',
    'query' : '${project_home}/sql/queries/issue_lifecycle.sql',
    'output': '${project_home}/dist/capex_alloc.csv',
    'format': 'csv'
}

def init_report(context: ReportContext):
    return __rep_config