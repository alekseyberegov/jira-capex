
delete from jira_issues 

drop table jira_issues 


select count(1) from jira_ol jo 

select max(KEY) from jira_ol jo 


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

select *
from jira_issues ji 
where points_meas = 21

select assignee_id, assignee_name, count(1)
from jira_issues ji 
group by 1, 2
order by 2, 1

select resolution_name,  count(1)
from jira_issues ji 
group by 1
order by 1
	