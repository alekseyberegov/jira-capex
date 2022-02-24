table = 'jira_ol'

# Primary key
primary_key = 'id'

# Foreign keys
foreign_keys = [
    'parent_id',
    'priority_id', 
    'status_id', 
    'issue_type_id',
    'project_id'
]

# Date fields
date_fields = ['status_change_date', 'created_date', 'updated_date']

fields_map = {
    'fields_parent_id' :                                    'parent_id',
    'fields_parent_key' :                                   'parent_key',
    'fields_parent_self' :                                  'parent_url',
    'fields_parent_fields_summary' :                        'parent_summary',
    'id':                                                   'id',
    'self':                                                 'url',
    'key':                                                  'key',
    'fields_statuscategorychangedate':                      'status_change_date',
    'fields_priority_name' :                                'priority_name',
    'fields_priority_id' :                                  'priority_id',
    'fields_status_name' :                                  'status_name',
    'fields_status_id' :                                    'status_id',
    'fields_creator_accountId':                             'creator_account_id',
    'fields_creator_emailAddress' :                         'creator_email',
    'fields_creator_displayName' :                          'creator_name',
    'fields_creator_timeZone' :                             'creator_timezone',
    'fields_reporter_accountId' :                           'reporter_account_id',
    'fields_reporter_emailAddress' :                        'reporter_email',
    'fields_reporter_displayName' :                         'reporter_name',
    'fields_reporter_timeZone' :                            'reporter_timezone',
    'fields_issuetype_id' :                                 'issue_type_id',
    'fields_issuetype_name' :                               'issue_type_name',
    'fields_issuetype_description' :                        'issue_type_desc',
    'fields_issuetype_subtask' :                            'issue_type_subtask',
    'fields_issuetype_hierarchyLevel' :                     'issue_type_hierarchy',
    'fields_project_id' :                                   'project_id',
    'fields_project_key' :                                  'project_key',
    'fields_project_projectTypeKey' :                       'project_type',
    'fields_created' :                                      'created_date',
    'fields_updated' :                                      'updated_date',
    'fields_duedate' :                                      'due_date',
    'fields_summary' :                                      'summary',
    'fields_description_type' :                             'desc_type',
    'fields_description_content_0_type' :                   'content_type',
    'fields_description_content_0_content_0_type' :         'content_type_0_type',
    'fields_description_content_0_content_0_text' :         'content_type_0_text'
}
