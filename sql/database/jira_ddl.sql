CREATE TABLE jira_status (
	id INTEGER,
	issue_id INTEGER,
	author_id INTEGER,
	author_name VARCHAR(250),
	created_date DATE,
	status_from VARCHAR(250),
	status_name_from INTEGER,
	status_to INTEGER,
	status_name_to INTEGER,
	CONSTRAINT jira_status_PK PRIMARY KEY (id)
);

CREATE TABLE jira_nord_terms (
	term VARCHAR(80),
	CONSTRAINT jira_nord_terms_PK PRIMARY KEY (term)	
);

CREATE TABLE jira_support_issues (
    issue_key VARCHAR(20),
    CONSTRAINT jira_support_issues_PK PRIMARY KEY (issue_key)
);


CREATE TABLE jira_former_employees (
	id VARCHAR(100),
	name VARCHAR(100),
	CONSTRAINT jira_former_employees_PK PRIMARY KEY (id)
);

CREATE TABLE jira_ol (
	parent_id INTEGER, 
	parent_key VARCHAR(120), 
	parent_url VARCHAR(120), 
	parent_summary VARCHAR(120), 
	id INTEGER NOT NULL, 
	url VARCHAR(120), 
	"key" VARCHAR(120), 
	status_change_date DATE, 
	priority_name VARCHAR(120), 
	priority_id INTEGER, 
	status_name VARCHAR(120), 
	status_id INTEGER, 
	creator_account_id VARCHAR(120), 
	creator_email VARCHAR(120), 
	creator_name VARCHAR(120), 
	creator_timezone VARCHAR(120), 
	reporter_account_id VARCHAR(120), 
	reporter_email VARCHAR(120), 
	reporter_name VARCHAR(120), 
	reporter_timezone VARCHAR(120), 
	issue_type_id INTEGER, 
	issue_type_name VARCHAR(120), 
	issue_type_desc VARCHAR(120), 
	issue_type_subtask VARCHAR(120), 
	issue_type_hierarchy VARCHAR(120), 
	project_id INTEGER, 
	project_key VARCHAR(120), 
	project_type VARCHAR(120), 
	created_date DATE, 
	updated_date DATE, 
	due_date DATE, 
	summary VARCHAR(120), 
	desc_type VARCHAR(120), 
	content_type VARCHAR(120), 
	content_type_0_type VARCHAR(120), 
	content_type_0_text VARCHAR(120), 
	PRIMARY KEY (id)
);

CREATE TABLE jira_issues (
	id INTEGER NOT NULL, 
	url VARCHAR(250), 
	"key" VARCHAR(250), 
	status_change_date DATE, 
	parent_id INTEGER, 
	parent_key VARCHAR(250), 
	parent_url VARCHAR(250), 
	parent_summary VARCHAR(250), 
	parent_issuetype_id INTEGER, 
	parent_issuetype_name VARCHAR(250), 
	parent_priority_name VARCHAR(250), 
	parent_priority_id INTEGER, 
	parent_status_id INTEGER, 
	parent_status_key VARCHAR(250), 
	resolution_name VARCHAR(250), 
	resolution_description VARCHAR(250), 
	resolution_date DATE, 
	priority_name VARCHAR(250), 
	priority_id INTEGER, 
	assignee_id VARCHAR(250), 
	assignee_email VARCHAR(250), 
	assignee_name VARCHAR(250), 
	assignee_timezone VARCHAR(250), 
	status_name VARCHAR(250), 
	status_id INTEGER, 
	points_meas FLOAT, 
	creator_id VARCHAR(250), 
	creator_email VARCHAR(250), 
	creator_name VARCHAR(250), 
	reporter_id VARCHAR(250), 
	reporter_email VARCHAR(250), 
	reporter_name VARCHAR(250), 
	issue_type_id INTEGER, 
	issue_type_name VARCHAR(250), 
	issue_type_subtask VARCHAR(250), 
	project_id INTEGER, 
	project_key VARCHAR(250), 
	project_name VARCHAR(250), 
	project_type VARCHAR(250), 
	created_date DATE, 
	updated_date DATE, 
	"description" VARCHAR(250), 
	summary VARCHAR(250), 
	due_date VARCHAR(250), 
	content_type VARCHAR(250), 
	content_type_0_type VARCHAR(250), 
	content_type_0_text VARCHAR(250), 
	snapshot_date DATE,
	capex_category varchar(250),
	project_driver varchar(250),
	assignee_id VARCHAR(250),
	assignee_email VARCHAR(250),
	assignee_name VARCHAR(250),
	assignee_timezone VARCHAR(250),
	creator_id VARCHAR(250),
	esolution_date DATE,
	resolution_name VARCHAR(250),
	resolution_description VARCHAR(250),
	snapshot_date DATE,
	content_len INTEGER,
	PRIMARY KEY (id)
);

CREATE TABLE jira_changelog (
	author_id VARCHAR(250), 
	author_name VARCHAR(250), 
	created_date DATE, 
	id INTEGER NOT NULL, 
	issue_id INTEGER, 
	items_0_field_name VARCHAR(250), 
	items_0_field_id VARCHAR(250), 
	items_0_field_type VARCHAR(250), 
	items_0_from VARCHAR(250), 
	items_0_from_text VARCHAR(250), 
	items_0_to VARCHAR(250), 
	items_0_to_text VARCHAR(250), 
	items_1_field_name VARCHAR(250), 
	items_1_field_id VARCHAR(250), 
	items_1_field_type VARCHAR(250), 
	items_1_from VARCHAR(250), 
	items_1_from_text VARCHAR(250), 
	items_1_to VARCHAR(250), 
	items_1_to_text VARCHAR(250), 
	items_2_field_name VARCHAR(250), 
	items_2_field_id VARCHAR(250), 
	items_2_field_type VARCHAR(250), 
	items_2_from VARCHAR(250), 
	items_2_from_text VARCHAR(250), 
	items_2_to VARCHAR(250), 
	items_2_to_text VARCHAR(250), 
	items_3_field_name VARCHAR(250), 
	items_3_field_id VARCHAR(250), 
	items_3_field_type VARCHAR(250), 
	items_3_from VARCHAR(250), 
	items_3_from_text VARCHAR(250), 
	items_3_to VARCHAR(250), 
	items_3_to_text VARCHAR(250), 
	items_4_field_name VARCHAR(250), 
	items_4_field_id VARCHAR(250), 
	items_4_field_type VARCHAR(250), 
	items_4_from VARCHAR(250), 
	items_4_from_text VARCHAR(250), 
	items_4_to VARCHAR(250), 
	items_4_to_text VARCHAR(250), 
	items_len INTEGER,
	snapshot_date DATE, 
	items_5_field_name VARCHAR(250), 
	items_5_field_id VARCHAR(250), 
	items_5_field_type VARCHAR(250), 
	items_5_from VARCHAR(250), 
	items_5_from_text VARCHAR(250), 
	items_5_to VARCHAR(250), 
	items_5_to_text VARCHAR(250), 
	items_6_field_name VARCHAR(250), 
	items_6_field_id VARCHAR(250), 
	items_6_field_type VARCHAR(250), 
	items_6_from VARCHAR(250), 
	items_6_from_text VARCHAR(250), 
	items_6_to VARCHAR(250), 
	items_6_to_text VARCHAR(250), 
	items_7_field_name VARCHAR(250), 
	items_7_field_id VARCHAR(250), 
	items_7_field_type VARCHAR(250), 
	items_7_from VARCHAR(250), 
	items_7_from_text VARCHAR(250), 
	items_7_to VARCHAR(250), 
	items_7_to_text VARCHAR(250), 
	items_8_field_name VARCHAR(250), 
	items_8_field_id VARCHAR(250), 
	items_8_field_type VARCHAR(250), 
	items_8_from VARCHAR(250), 
	items_8_from_text VARCHAR(250), 
	items_8_to VARCHAR(250), 
	items_8_to_text VARCHAR(250), 
	items_9_field_name VARCHAR(250), 
	items_9_field_id VARCHAR(250), 
	items_9_field_type VARCHAR(250), 
	items_9_from VARCHAR(250), 
	items_9_from_text VARCHAR(250), 
	items_9_to VARCHAR(250), 
	items_9_to_text VARCHAR(250), 
	PRIMARY KEY (id)
);

create table jira_issue_lifecycle (
	issue_id				INTEGER NOT NULL,
	issue_key				VARCHAR(250),
	status_name				VARCHAR(250),
	resolution_name			VARCHAR(250),
	status_log				VARCHAR(4000),
	issue_created			DATE,
	issue_updated			DATE,
	status_updated			DATE,
	resolution_created		DATE,
	issue_started			DATE,
	issue_completed			DATE,
	work_started			DATE,
	work_ended				DATE,
	PRIMARY KEY (issue_id)
);
