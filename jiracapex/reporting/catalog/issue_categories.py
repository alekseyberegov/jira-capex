import pandas as pd
from jiracapex.reporting.context import ReportContext

__rep_config = {
    'report' : 'issue_categories',
    'source' : {'type': 'file', 'uri' : '${project_home}/data/csv/issue_categories_${crunch_date}.csv', 'options': {}},
    'target' : {'type':  None, 'uri' : None, 'options': {}},
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
