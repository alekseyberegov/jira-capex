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


