select JULIANDAY(end_date) - JULIANDAY(start_date) + 1 as duration, *
from (
	select COALESCE(work_started, issue_started, issue_created) as start_date
		,  COALESCE(work_ended, issue_completed) as end_date
		, ji.*
	from jira_issue_lifecycle  ji
) d
order by 1 desc
limit 100

