# Table name
table = 'jira_issues'

# Primary key
primary_key = 'id'

# Foreign keys
foreign_keys = [
    'parent_id',
    'priority_id', 
    'status_id', 
    'issue_type_id',
    'project_id',
    'parent_issuetype_id',
    'parent_priority_id',
    'parent_status_id'
]

# Date fields
date_fields = ['status_change_date', 'created_date', 'updated_date', 'resolution_date']

# Felds mapping
fields_map = {
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
    'fields_resolutiondate':                                'resolution_date', # Example: 2018-09-20T15:45:57.937-0500
    'fields_customfield_10022':                             'points_meas', # Example: 1.0
    'fields_description':                                   'description',     
    'fields_description_content_0_type' :                   'content_type',
    'fields_description_content_0_content_0_type' :         'content_type_0_type',
    'fields_description_content_0_content_0_text' :         'content_type_0_text'
}