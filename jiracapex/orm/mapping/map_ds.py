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

fields_map = {
    'id':                                               'id', 
    'self':                                             'url', 
    'key':                                              'key', 
    'fields_statuscategorychangedate':                  'status_change_date',
    'fields_parent_id':                                 'parent_id',
    'fields_parent_key':                                'parent_key',
    'fields_parent_self':                               'parent_url',
    'fields_parent_fields_summary':                     'parent_summary', 
    'fields_parent_fields_issuetype_id':                'parent_issuetype_id',
    'fields_parent_fields_issuetype_name':              'parent_issuetype_name', 
    'fields_parent_fields_priority_name':               'parent_priority_name', 
    'fields_parent_fields_priority_id':                 'parent_priority_id',
    'fields_parent_fields_status_statusCategory_id':    'parent_status_id',
    'fields_parent_fields_status_statusCategory_key':   'parent_status_key', 
    'fields_resolution_name':                           'resolution_name', 
    'fields_resolution_description':                    'resolution_description',
    'fields_resolutiondate':                            'resolution_date',
    'fields_priority_name':                             'priority_name', 
    'fields_priority_id':                               'priority_id', 
    'fields_assignee_accountId':                        'assignee_id',
    'fields_assignee_emailAddress':                     'assignee_email', 
    'fields_assignee_displayName':                      'assignee_name', 
    'fields_assignee_timeZone':                         'assignee_timezone',
    'fields_status_name':                               'status_name',
    'fields_status_id':                                 'status_id', 
    'fields_customfield_10022':                         'points_meas',
    'fields_creator_accountId':                         'creator_id',
    'fields_creator_emailAddress':                      'creator_email',
    'fields_creator_displayName':                       'creator_name', 
    'fields_reporter_accountId':                        'reporter_id', 
    'fields_reporter_emailAddress':                     'reporter_email',
    'fields_reporter_displayName':                      'reporter_name',
    'fields_issuetype_id':                              'issue_type_id', 
    'fields_issuetype_name':                            'issue_type_name',
    'fields_issuetype_subtask':                         'issue_type_subtask',
    'fields_project_id':                                'project_id',
    'fields_project_key':                               'project_key', 
    'fields_project_name':                              'project_name', 
    'fields_project_projectTypeKey':                    'project_type', 
    'fields_created':                                   'created_date', 
    'fields_updated':                                   'updated_date', 
    'fields_description':                               'description', 
    'fields_summary':                                   'summary',
    'fields_duedate':                                   'due_date',
    'fields_description_content_0_type' :               'content_type',
    'fields_description_content_0_content_0_type' :     'content_type_0_type',
    'fields_description_content_0_content_0_text' :     'content_type_0_text'
}