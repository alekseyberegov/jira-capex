
delete from jira_issues 

drop table jira_issues 


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

	
select points_meas , count(1)
from jira_issues ji 
group by 1

select id, "key", *
from jira_issues ji 

select assignee_id, assignee_name, count(1) as cnt
from jira_issues ji 
group by 1, 2
order by 3 desc

select project_name, project_key , status_name, resolution_name ,  count(1)
from jira_issues ji 
group by 1, 2, 3
order by 1, 2, 3


drop table jira_changelog1 
	

select count(1) as cnt
, count(distinct issue_id) as issue_cnt
from jira_changelog

select i.*
from jira_issues i 
where i.id not in (select distinct issue_id from jira_changelog)

select * from jira_issues ji  where id = 56756

	
	select status_id, status_name, count(1)
	from jira_issues ji 
	group by 1,2
	
--	Employee Name
--	Task ID
--	Task Name 
--	Task Description
--	Task 'Points'
--	Associated OL Project (or 'None')
--	OL Project Description (?)
--	Effective Start Work
--	Effective End Work
--	Task Creation Date
--	Task Close Date
--	Task Last Update
	select *, julianday(end_date) - julianday(start_date) + 1  as days_spent
	from (
		select COALESCE(ji.assignee_id, ji.creator_id) as emp_id
			, COALESCE(ji.assignee_name, ji.creator_name)  as emp_name
			, ji."key" as task_id
			, ji.summary as task_name
			, ji.points_meas as points
			, case when ji.points_meas is not null then round(-2.860678277+points_meas*3.887259395,0) else 2 end as efforts
			, parent_key as project_id
			, parent_summary  as project_desc
			, case when inprogress_date is not null and inprogress_date > st.start_date then inprogress_date else start_date end as start_date
			, case when closed_date is not null and closed_date < end_date then closed_date else end_date end as end_date  
			, ji.created_date  
			, ji.updated_date 
			, ji.status_change_date 
			, ji.status_name 
			, ji.resolution_name 
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
		order by 2, 1
	)
	where status_name <> 'Won''t Do' 
		and resolution_name <> 'Won''t Do' 
			and resolution_name <> 'Cannot Reproduce' 
				and resolution_name <> 'Duplicate'
					and start_date between '2021-01-01' and '2022-01-01'
					

	select 1 , status_name, count(1)
	from jira_issues ji 
	group by 1,2
	

	
	--
	-- Chase no R&D
	--
	select emp_id
			, emp_name
			, task_id
			, task_name
			, (case when task_id like 'IEN-%' or project_id like 'IEN-%' or (project_id is null 
					and (terms_cnt > 0 or exclude_cnt > 0)) then 'Yes' else 'No' end) as is_support
			, points
			, efforts
			, project_id
			, project_desc
			, start_date
			, end_date
			, created_date  
			, updated_date 
			, status_change_date 
			, status_name 
			, resolution_name 
		, julianday(end_date) - julianday(start_date) + 1  as days_spent
	from (
		select COALESCE(ji.assignee_id, ji.creator_id) as emp_id
			, COALESCE(ji.assignee_name, ji.creator_name)  as emp_name
			, ji."key" as task_id
			, lower(ji.summary) as task_name
			, ji.points_meas as points
			, case when ji.points_meas is not null then round(-2.860678277+points_meas*3.887259395,0) else 2 end as efforts
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
		order by 2, 1
	) d
	where status_name <> 'Won''t Do' 
		and resolution_name <> 'Won''t Do' 
			and resolution_name <> 'Cannot Reproduce' 
				and resolution_name <> 'Duplicate'
					and start_date between '2020-01-01' and '2021-01-01'
			
							
select *
from jira_nord_terms 
where term like 'issu%'

select * from jira_support_issues