
select count(1)
from jira_issues ji 


select count(1)
from jira_changelog jc 

select count(1)
from jira_status js 




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


select 'map_'||lower(project_key), count(1), max(created_date)
from jira_issues ji 
group by 1

SELECT assignee_email, assignee_name, created_date  , *
FROM jira_issues
WHERE "key" like 'TWR%'
	and assignee_name = 'Noelle Laureano'

-- ===========================
--
-- Expected vs Actual counts
--
-- ===========================
select *, max_key - min_key + 1 as expected_cnt
from (
	select project_key
		,  min(cast(substr(key,instr(key, '-') + 1) as integer)) as min_key
		,  max(cast(substr(key,instr(key, '-') + 1) as integer)) as max_key
		,  count(1) as cnt
	from jira_issues ji 
	group by 1
)

select project_key,  max(created_date), min(created_date)
from jira_issues ji 
group by 1

delete from jira_issues where created_date >= '2022-01-01'

select created_date, *
from jira_ol jo 
order by 1 desc

WITH RECURSIVE generate_series(value) AS (
  SELECT 3052
  UNION ALL
  SELECT value+1 FROM generate_series
   WHERE value+1 <= 6053
)
select *
from (
	SELECT value, i.key
	FROM generate_series g
		left join jira_issues i on (g.value = cast(substr(key,instr(key, '-') + 1) as integer))
) where key is null

	--
	-- Report
	--
	select emp_id
			, emp_name
			, task_id
			, task_name
			, (case when task_id like 'IEN-%' or project_id like 'IEN-%' or (project_id is null 
					and (terms_cnt > 0 or exclude_cnt > 0)) then 'Yes' else 'No' end) as is_support
			, points
			, case when points > 0 then round(-2.860678277+points*3.887259395,0) else 2 end as efforts
			, project_id
			, project_desc
			, start_date
			, end_date
			, created_date  
			, updated_date 
			, status_change_date 
			, status_name 
			, resolution_name 
		, julianday(end_date) - julianday(start_date  ) + 1 as days_spent
		, julianday(end_date) - julianday(created_date) + 1 as lifespan
		, last_points
	from (
		select COALESCE(ji.assignee_id, ji.creator_id) as emp_id
			, COALESCE(e.name, ji.assignee_name, ji.creator_name)  as emp_name
			, ji."key" as task_id
			, lower(ji.summary) as task_name
			, max(ifnull(ji.points_meas,0), ifnull(pc.max_from,0), ifnull(pc.max_to,0)  ) as points
			, ji.points_meas as last_points
			, parent_key as project_id
			, parent_summary  as project_desc
			, case when inprogress_date is not null and inprogress_date > st.start_date then inprogress_date else start_date end as start_date
			, case when closed_date is not null and closed_date < end_date then closed_date else end_date end as end_date  
			, ji.created_date  
			, ji.updated_date 
			, ji.status_change_date 
			, ji.status_name 
			, ji.resolution_name 
			, (select count(1) from jira_nord_terms  where instr( lower(ji.summary), term)) as terms_cnt
			, (select count(1) from jira_support_issues where ji."key" = issue_key) as exclude_cnt
		from jira_issues ji 
			left join (
					select issue_id
						, min(created_date) as start_date
						, max(created_date) as end_date
						, max(case when status_name_to = 'Closed' then created_date end) as closed_date
						, max(case when status_name_to = 'In Progress' then created_date end) as inprogress_date
					from jira_status js 
					where status_name_to in ('Done', 'In Progress', 'Closed', 'Implementing', 'Released', 'Solved', 'Finished')
					group by 1
			) st on (st.issue_id = ji.id)
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
				)
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
					and start_date between '2021-01-01' and '2022-01-01'
						and created_date >= '2020-01-01'
					

select * from jira_former_employees;				
					
select id
	, "key"
	, status_name
	, resolution_name
	, created_date	
	, updated_date	
	, status_change_date
	, status_history
from jira_issues ji 
left join (
	select js.issue_id, GROUP_CONCAT(js.status_name_to ||':'||js.created_date, ',') as status_history  
	from jira_status js  
	group by 1
) hs on (ji.id = hs.issue_id)
	
select 
from jira_status js 
group by 1

			
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
)
where lower(nm) like '%points%'
group by 1
