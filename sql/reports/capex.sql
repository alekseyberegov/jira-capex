select emp_id
	, emp_name
	, task_id
	, task_name
	, capex_category
	, (case when (capex_category is not null and capex_category = 'No Capitalization' ) 
		or  task_id like 'IEN-%' 
			or project_id like 'IEN-%' 
				or (project_id is null and (terms_cnt > 0 or exclude_cnt > 0)) then 'Yes' else 'No' end) as is_support
	, points
	, case when points > 0 then round(-2.860678277+points*3.887259395,0) else 2 end as efforts
	, project_id
	, project_driver
	, project_desc
	, beg_date
	, end_date
	, created_date  
	, updated_date 
	, status_change_date 
	, status_name 
	, resolution_name 
	, julianday(end_date) - julianday(beg_date    ) + 1 as days_spent
	, julianday(end_date) - julianday(created_date) + 1 as lifespan
	, last_points
	, status_log
from (
		select COALESCE(ji.assignee_id, ji.creator_id) as emp_id
			, COALESCE(e.name, ji.assignee_name, ji.creator_name)  as emp_name
			, ji."key" as task_id
			, lower(ji.summary) as task_name
			, max(ifnull(ji.points_meas,0), ifnull(pc.max_from,0), ifnull(pc.max_to,0)) as points
			, ji.points_meas as last_points
			, ji.parent_key as project_id
			, ji.parent_summary  as project_desc
			, jo.capex_category 
			, jo.project_driver 
			, COALESCE(work_started, issue_started, issue_created) as beg_date
			, COALESCE(work_ended, issue_completed) as end_date
			, ji.created_date  
			, ji.updated_date 
			, ji.status_change_date 
			, ji.status_name 
			, ji.resolution_name 
			, (select count(1) from jira_nord_terms  where instr( lower(ji.summary), term) > 0) as terms_cnt
			, (select count(1) from jira_support_issues where ji."key" = issue_key) as exclude_cnt
			, jil.status_log 
		from jira_issues ji 
			left join jira_issue_lifecycle jil on (jil.issue_id = ji.id)
			left join jira_ol jo on (jo.id = ji.parent_id)
			left join (
				select issue_id
				, max(cast(ifnull(from_txt,0) as int) )  as max_from
				, max(cast(to_txt as int) ) as max_to
				from (
					select items_0_field_name as nm, issue_id, jc.items_0_from_text as from_txt,  jc.items_0_to_text as to_txt
					from jira_changelog jc 
					union all
					select items_1_field_name as nm, issue_id, jc.items_1_from_text as from_txt,  jc.items_1_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_2_field_name as nm, issue_id, jc.items_2_from_text as from_txt,  jc.items_2_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_3_field_name as nm, issue_id, jc.items_3_from_text as from_txt,  jc.items_3_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_4_field_name as nm, issue_id, jc.items_4_from_text as from_txt,  jc.items_4_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_5_field_name as nm, issue_id, jc.items_5_from_text as from_txt,  jc.items_5_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_6_field_name as nm, issue_id, jc.items_6_from_text as from_txt,  jc.items_6_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_7_field_name as nm, issue_id, jc.items_7_from_text as from_txt,  jc.items_7_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_8_field_name as nm, issue_id, jc.items_8_from_text as from_txt,  jc.items_8_to_text as to_txt
					from jira_changelog jc 
					union ALL 
					select items_9_field_name as nm, issue_id, jc.items_9_from_text as from_txt,  jc.items_9_to_text as to_txt
					from jira_changelog jc 
				) d
				where lower(nm) like '%points%'
				group by 1
			) pc on (pc.issue_id = ji.id)
			left join jira_former_employees e on (COALESCE(ji.assignee_id, ji.creator_id) = e.id)
		order by 2, 1
	) d 
where status_name <> 'Won''t Do' 
		and IFNULL(resolution_name, 'Empty') <> 'Won''t Do' 
			and IFNULL(resolution_name, 'Empty') <> 'Cannot Reproduce' 
				and IFNULL(resolution_name, 'Empty') <> 'Duplicate'
					and end_date >= '2022-01-01'
						and created_date < '2022-07-01'
	
