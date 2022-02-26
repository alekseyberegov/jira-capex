from typing import Dict, List

BLOCKED_FIELDS: List[str] = [
    'fields_parent_fields_status_self',
    'fields_parent_fields_status_description',
    'fields_parent_fields_status_name',
    'fields_parent_fields_issuetype_subtask',
    'fields_priority_self',
    'fields_environment',
    'fields_security',
    'fields_issuetype_description'
]

DEFAULT_FIELD_MAPPING: Dict[str, str] = {
    'fields_parent_id' :                                    'parent_id',
    'fields_parent_key' :                                   'parent_key',
    'fields_parent_self' :                                  'parent_url',
    'fields_parent_fields_summary' :                        'parent_summary',
    'id':                                                   'id',
    'self':                                                 'url',
    'key':                                                  'key',
    'fields_statuscategorychangedate':                      'status_change_date',   # Example: 2022-02-15T12:34:27.520-0600
    'fields_priority_name' :                                'priority_name',
    'fields_priority_id' :                                  'priority_id',
    'fields_status_name' :                                  'status_name',
    'fields_status_id' :                                    'status_id',
    'fields_assignee_accountId':                            'assignee_id', # 5e0e93d362aed90daa48adf8
    'fields_assignee_emailAddress':                         'assignee_email', # jeff@clicktripz.com
    'fields_assignee_displayName':                          'assignee_name', # Jeff McDonald
    'fields_assignee_timeZone':                             'assignee_timezone', # America/Los_Angeles
    'fields_status_name':                                   'status_name', # Scheduled
    'fields_creator_accountId':                             'creator_id',
    'fields_creator_emailAddress' :                         'creator_email',
    'fields_creator_displayName' :                          'creator_name',
    'fields_creator_timeZone' :                             'creator_timezone',
    'fields_reporter_accountId' :                           'reporter_id',
    'fields_reporter_emailAddress' :                        'reporter_email',
    'fields_reporter_displayName' :                         'reporter_name',
    'fields_reporter_timeZone' :                            'reporter_timezone',
    'fields_issuetype_id' :                                 'issue_type_id',
    'fields_issuetype_name' :                               'issue_type_name',
    'fields_issuetype_subtask' :                            'issue_type_subtask',
    'fields_issuetype_hierarchyLevel' :                     'issue_type_hierarchy',
    'fields_project_id' :                                   'project_id',
    'fields_project_key' :                                  'project_key',
    'fields_project_projectTypeKey' :                       'project_type',
    'fields_created' :                                      'created_date', # Example: 2022-01-20T17:05:36.638-0600
    'fields_updated' :                                      'updated_date', # Example: 2022-02-15T12:34:27.520-0600
    'fields_duedate' :                                      'due_date',
    'fields_summary' :                                      'summary',
    'fields_description_type' :                             'desc_type',
    'fields_resolution':                                    'resolution', 
    'fields_customfield_10022':                             'points_meas' # 1.0
}