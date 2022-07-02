select JULIANDAY(end_date) - JULIANDAY(beg_date) + 1 as duration, *
from (
	select COALESCE(work_started, issue_started, issue_created) as beg_date
		,  COALESCE(work_ended, issue_completed) as end_date
		, ji.*
	from jira_issue_lifecycle  ji
) d
where end_date >= '${crunch_date}'
	and beg_date < DATE('${crunch_date}','+1 year')
order by 1 desc
