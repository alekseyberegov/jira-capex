
delete from jira_issues 

drop table jira_issues 


select count(1) from jira_ol jo 

select max(KEY) from jira_ol jo 


select count(1) from jira_issues ji 


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

select * from jira_issues ji  where id = 56756