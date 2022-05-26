
INSERT into jira_status(id, status_name_from, status_from, status_name_to, status_to, issue_id, created_date , author_id, author_name )
		select id
					, case when items_0_field_name = 'status' then items_0_from_text
						when items_1_field_name = 'status' then items_1_from_text
						when items_2_field_name = 'status' then items_2_from_text
						when items_3_field_name = 'status' then items_3_from_text
						when items_4_field_name = 'status' then items_4_from_text			
					end as status_name_from
					, case when items_0_field_name = 'status' then items_0_from
						when items_1_field_name = 'status' then items_1_from
						when items_2_field_name = 'status' then items_2_from
						when items_3_field_name = 'status' then items_3_from
						when items_4_field_name = 'status' then items_4_from		
					end as status_from
					, case when items_0_field_name = 'status' then items_0_to_text
						when items_1_field_name = 'status' then items_1_to_text
						when items_2_field_name = 'status' then items_2_to_text
						when items_3_field_name = 'status' then items_3_to_text
						when items_4_field_name = 'status' then items_4_to_text			
					end as status_name_to
					, case when items_0_field_name = 'status' then items_0_to
						when items_1_field_name = 'status' then items_1_to
						when items_2_field_name = 'status' then items_2_to
						when items_3_field_name = 'status' then items_3_to
						when items_4_field_name = 'status' then items_4_to	
					end as status_to
				, issue_id
				, created_date 
				, author_id
				, author_name
			from jira_changelog 
			where items_0_field_name = 'status'
				or items_1_field_name = 'status'
					or items_2_field_name = 'status'
						or items_3_field_name = 'status'
							or items_4_field_name = 'status'
							
							
							

alter table jira_ol add column capex_category varchar(250);
alter table jira_ol add column project_driver varchar(250);
alter table jira_ol add column assignee_id VARCHAR(250);
alter table jira_ol add column assignee_email VARCHAR(250);
alter table jira_ol add column assignee_name VARCHAR(250);
alter table jira_ol add column assignee_timezone VARCHAR(250);
alter table jira_ol add column creator_id VARCHAR(250);
alter table jira_ol add column resolution_date DATE;
alter table jira_ol add column resolution_name VARCHAR(250);
alter table jira_ol add column resolution_description VARCHAR(250);
