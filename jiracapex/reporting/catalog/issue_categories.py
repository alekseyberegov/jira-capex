import pandas as pd
from jiracapex.reporting.context import ReportContext

CATEGORY_NO_CAPEX: str = 'Not Classified to CapEx Category'

def calc_capex(x):
    x = x.dropna()
    capex: int = sum(v for k,v in x.to_dict().items() if k.startswith('ct_') and k != 'ct_no_capex') 
    task_cat: str = x.get('task_category', 'n/a')
    task_exp: int = x.get('ct_no_capex'  , 0)

    if x.task_id.startswith('ARCH') \
        or x.is_support.upper() == 'YES' \
            or task_exp == 1 \
                or task_cat == CATEGORY_NO_CAPEX:
        if capex > 0: capex = -1
    else:
        if capex == 0 and task_cat != 'n/a': capex = 1
        if capex == 0: capex = -1

    return capex

__rep_config = {
    'report' : 'issue_categories',
    'source' : {'type': 'file', 'uri' : '${project_home}/data/csv/issue_categories_${crunch_date}.csv', 'options': {}},
    'target' : {'type': 'dbms', 'uri' : 'jira_category_${__func_norm:crunch_date}', 'options': {}},
    'schema' : {
        'Auctions Algo Enhancements'        : {'name': 'ct_auction_algo', 'type': 'float'},
        'B/W Box Automated Testing'         : {'name': 'ct_testing_auto', 'type': 'float'},
        'Bidding Automation'                : {'name': 'ct_bidding_auto', 'type': 'float'},
        'CTI'                               : {'name': 'ct_cti'         , 'type': 'float'},
        'Conversion Booster'                : {'name': 'ct_conv_booster', 'type': 'float'},
        'Dynamic Display'                   : {'name': 'ct_dynamic_disp', 'type': 'float'},
        'ETL'                               : {'name': 'ct_etl'         , 'type': 'float'},
        'Exit Unit Product Enhancements'    : {'name': 'ct_exit_unit'   , 'type': 'float'},
        'Integrations Infrastructure'       : {'name': 'ct_integrations', 'type': 'float'},
        'Internal Data Analytics'           : {'name': 'ct_analytics'   , 'type': 'float'},
        'Machine Learning'                  : {'name': 'ct_ml'          , 'type': 'float'},
        'Meta Search and Mapping'           : {'name': 'ct_mapping'     , 'type': 'float'},
        'Mobile Solutions'                  : {'name': 'ct_mobile'      , 'type': 'float'},
        'Not Classified to CapEx Category'  : {'name': 'ct_no_capex'    , 'type': 'float'},
        'Other Data Infrastructure'         : {'name': 'ct_other_data'  , 'type': 'float'},
        'task_id'                           : {'type': 'str'  },
        'created_date'                      : {'type': 'date' },
        'efforts'                           : {'type': 'int'  },
        'emp_id'                            : {'type': 'str'  },
        'emp_name'                          : {'type': 'str'  },
        'is_support'                        : {'type': 'str'  },
        'task_category'                     : {'type': 'str'  },
        'last_points'                       : {'type': 'float'},
        'points'                            : {'type': 'float'},
        'project_desc'                      : {'type': 'str'  },
        'project_id'                        : {'type': 'str'  },
        'resolution_name'                   : {'type': 'str'  },
        'status_name'                       : {'type': 'str'  },
        'task_name'                         : {'type': 'str'  },
        'updated_date'                      : {'type': 'date' }
    },
    'derive' : [
        {
            'name': 'capex_ind',
            'calc': calc_capex
        }
    ],
    'index'  : 'task_id'
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
