from jiracapex.reporting.context import ReportContext

__rep_config = {
    'report' : 'jira_gusto_map',
    'source' : {'type': 'file', 'uri' : '${project_home}/data/csv/jira_gusto_map.csv', 'options': {}},
    'target' : {'type': 'dbms', 'uri' : 'jira_gusto', 'options': {}},
    'index'  : 'jira_emp_name'
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)