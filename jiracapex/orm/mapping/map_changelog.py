# Table name
table = 'jira_changelog'

# Primary key
primary_key = 'id'

# Foreign keys
foreign_keys = ['issue_id']

# Date fields
date_fields = ['created_date']

fields_map = {  
    "author_accountId":         "author_id",
    "author_displayName":       "author_name",
    "created":                  "created_date", # Example 2019-01-08T12:40:37.081-0600
    "id":                       "id",
    "issue_id":                 "issue_id",
    "items_len":                "items_len",
    "items_0_field":            "items_0_field_name",
    "items_0_fieldId":          "items_0_field_id",
    "items_0_fieldtype":        "items_0_field_type",
    "items_0_from":             "items_0_from",
    "items_0_fromString":       "items_0_from_text",
    "items_0_to":               "items_0_to",
    "items_0_toString":         "items_0_to_text",
    "items_1_field":            "items_1_field_name",
    "items_1_fieldId":          "items_1_field_id",
    "items_1_fieldtype":        "items_1_field_type",
    "items_1_from":             "items_1_from",
    "items_1_fromString":       "items_1_from_text",
    "items_1_to":               "items_1_to",
    "items_1_toString":         "items_1_to_text",
    "items_2_field":            "items_2_field_name",
    "items_2_fieldId":          "items_2_field_id",
    "items_2_fieldtype":        "items_2_field_type",
    "items_2_from":             "items_2_from",
    "items_2_fromString":       "items_2_from_text",
    "items_2_to":               "items_2_to",
    "items_2_toString":         "items_2_to_text",
    "items_3_field":            "items_3_field_name",
    "items_3_fieldId":          "items_3_field_id",
    "items_3_fieldtype":        "items_3_field_type",
    "items_3_from":             "items_3_from",
    "items_3_fromString":       "items_3_from_text",
    "items_3_to":               "items_3_to",
    "items_3_toString":         "items_3_to_text",
    "items_4_field":            "items_4_field_name",
    "items_4_fieldId":          "items_4_field_id",
    "items_4_fieldtype":        "items_4_field_type",
    "items_4_from":             "items_4_from",
    "items_4_fromString":       "items_4_from_text",
    "items_4_to":               "items_4_to",
    "items_4_toString":         "items_4_to_text"
}