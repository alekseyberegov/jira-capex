from jiracapex.reporting.context import ReportContext

__rep_config = {
    'report' : 'employee_participation',
    'source' : {'type': 'file', 'uri' : '${project_home}/data/csv/employee_participation_${crunch_date}.csv', 'options': {}},
    'target' : {'type': 'dbms', 'uri' : 'employee_participation_${__func_norm:crunch_date}', 'options': {}},
    'derive' : [
        {
            'name': 'emp_name',
            'calc': lambda x: " ".join([x.first_name, x.last_name])
        }
    ]
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
