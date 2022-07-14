DELETE FROM jira_status;

SELECT count(1) FROM jira_status;


INSERT into jira_status(id, status_name_from, status_from, status_name_to, status_to, issue_id, created_date , author_id, author_name )
		select id
				 , case when items_0_field_name = 'status' then items_0_from_text
						when items_1_field_name = 'status' then items_1_from_text
						when items_2_field_name = 'status' then items_2_from_text
						when items_3_field_name = 'status' then items_3_from_text
						when items_4_field_name = 'status' then items_4_from_text	
						when items_5_field_name = 'status' then items_5_from_text
						when items_6_field_name = 'status' then items_6_from_text
						when items_7_field_name = 'status' then items_7_from_text
						when items_8_field_name = 'status' then items_8_from_text			
						when items_9_field_name = 'status' then items_9_from_text					
					end as status_name_from
				 , case when items_0_field_name = 'status' then items_0_from
						when items_1_field_name = 'status' then items_1_from
						when items_2_field_name = 'status' then items_2_from
						when items_3_field_name = 'status' then items_3_from
						when items_4_field_name = 'status' then items_4_from	
						when items_5_field_name = 'status' then items_5_from		
						when items_6_field_name = 'status' then items_6_from		
						when items_7_field_name = 'status' then items_7_from		
						when items_8_field_name = 'status' then items_8_from
						when items_9_field_name = 'status' then items_9_from			
					end as status_from
				 , case when items_0_field_name = 'status' then items_0_to_text
						when items_1_field_name = 'status' then items_1_to_text
						when items_2_field_name = 'status' then items_2_to_text
						when items_3_field_name = 'status' then items_3_to_text
						when items_4_field_name = 'status' then items_4_to_text		
						when items_5_field_name = 'status' then items_5_to_text	
						when items_6_field_name = 'status' then items_6_to_text	
						when items_7_field_name = 'status' then items_7_to_text	
						when items_8_field_name = 'status' then items_8_to_text	
						when items_9_field_name = 'status' then items_9_to_text		
					end as status_name_to
				 , case when items_0_field_name = 'status' then items_0_to
						when items_1_field_name = 'status' then items_1_to
						when items_2_field_name = 'status' then items_2_to
						when items_3_field_name = 'status' then items_3_to
						when items_4_field_name = 'status' then items_4_to	
						when items_5_field_name = 'status' then items_5_to	
						when items_6_field_name = 'status' then items_6_to	
						when items_7_field_name = 'status' then items_7_to	
						when items_8_field_name = 'status' then items_8_to	
						when items_9_field_name = 'status' then items_9_to	
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
									or items_5_field_name = 'status'
										or items_6_field_name = 'status'
											or items_7_field_name = 'status'
												or items_8_field_name = 'status'
													or items_9_field_name = 'status'
							

DELETE FROM jira_issue_lifecycle;

SELECT count(1) FROM jira_issue_lifecycle;

insert into jira_issue_lifecycle(
	  issue_id
	, issue_key
	, status_name
	, resolution_name
	, status_log
	, issue_created
	, issue_updated
	, status_updated
	, resolution_created
	, issue_started
	, issue_completed
	, work_started
	, work_ended)	
select issue_id
	, issue_key
	, status_name
	, resolution_name
	, '['||group_concat('{"s0":"'||s0||'","t0":"'||t0||'","s1":"'||s1||'","t1":"'||t1||'"}', ',')||']' as status_log
	, min(issue_created) as issue_created
	, max(issue_updated) as issue_updated
	, max(status_updated) as status_updated
	, max(resolution_date) as resolution_created
	, min(case when s0 in ('Scheduled', 'Open', 'Backlog', 'To Do') then t1 end) as issue_started
	, min(case when s1 in ('Done', 'Released', 'Accepted', 'Closed', 'Finished', 'Old Done') then t1 end) as issue_completed
	, min(case when from_progress = 1 then t0 end) as work_started
	, max(case when from_progress = 1 then t1 end) as work_ended
from (
	select issue_id
		, js.created_date as t1
		, IFNULL(lag(js.created_date) 
			over(partition by issue_id order by js.issue_id, js.created_date), ji.created_date) as t0
		, ji.created_date as issue_created
		, ji.updated_date as issue_updated
		, ji.status_change_date as status_updated
		, ji."key" as issue_key
		, ji.status_name 
		, ji.resolution_name 
		, ji.resolution_date 
		, case when status_name_from = 'In Progress' then 1 else 0 end as from_progress
		, js.status_name_from as s0
		, js.status_name_to   as s1
	from jira_status js inner join jira_issues ji on (js.issue_id = ji.id)
	where IFNULL(status_name, 'Unknown') not in ('Won''t Do') 
		and IFNULL(resolution_name, 'Unknown') not in ('Won''t Do', 'Duplicate')
	order by 1, 2
) d
group by 1, 2
