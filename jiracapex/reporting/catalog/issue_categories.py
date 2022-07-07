import pandas as pd
from jiracapex.reporting.context import ReportContext

CATEGORY_NO_CAPEX: str = 'Not Classified to CapEx Category'

# - If any Column in U to AH =1, then count task efforts in that respective CapEx category, otherwise
# - Count task efforts in the category labeled in Column T
# - Also, report any tasks for which columns T through AI are all empty, or columns U through AI sum to more than 1. 
# - Also, report any tasks for which columns T through AI are all empty (and "Is Support" = NO), 
#       or columns U through AI sum to more than 1. 
def calc_capex(df: pd.DataFrame):
    def func(x):
        capex: int = 0
        x = x.dropna()
        # - Also, report any tasks for which columns T through AI are all empty, or columns U through AI sum to more than 1.
        for c in x.keys():
            if c.startswith('ct_') and c != 'ct_no_capex':
                capex += x[c]
        cat: str = x.get('task_category', 'n/a')
        neg: int = x.get('ct_no_capex', 0)

        # - Ignore / do not count efforts for tickets containing "ARCH"
        # - If Column "Is Support" = Yes, then count task efforts as "Not Classified to CapEx Category"
        # - If Column "Not Classified to CapEx Category" = 1, then count task efforts as "Not Classified to CapEx Category"
        if x.name.startswith('ARCH') \
            or x.is_support.upper() == 'YES' \
                or neg == 1 \
                    or cat == CATEGORY_NO_CAPEX:
            if capex > 0: capex = -1
        else:
            # - If any Column in U to AH =1, then count task efforts in that respective CapEx category,
            if capex == 0 and cat != 'n/a': capex = 1
            if capex == 0: capex = -1

        return capex
    return df.apply(lambda x: func(x), axis=1)

__rep_config = {
    'report' : 'issue_categories',
    'source' : {'type': 'file', 'uri' : '${project_home}/data/csv/issue_categories_${crunch_date}.csv', 'options': {}},
    'target' : {'type': 'dbms', 'uri' : 'jira_category_${__func_norm:crunch_date}', 'options': {}},
    'index'  : 'task_id',
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
    ]
}

def __init__(context: ReportContext):
    return context.replace_obj(__rep_config)
