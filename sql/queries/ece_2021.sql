with recursive generate_series(value) AS (
  select 0
  union all
  select value + 1 from generate_series
  where value + 1 <= 11
)
select d.*
	, sum(efforts_category) over(partition by emp_name, month_date) as efforts_month
	, sum(efforts_category) over(partition by emp_name) as efforts_year
from (
	select emp_name
		, month_date
		, stamp
		, max(emp_total) as emp_contrib
		, max(e_m / emp_total) as w2_fraction
		, sum(IFNULL(efforts * t_m / duration,0)) as efforts_category
	from (
		select m.value as month_num
			, date(julianday('2021-01-01'), '+' || m.value || ' month') as month_date
			, w.*
			, IFNULL(json_extract(e_a,'$['||m.value||']'),0) as e_m
			, IFNULL(json_extract(t_a,'$['||m.value||']'),0) as t_m
		from (
				SELECT COALESCE(e.emp_name, c.emp_name) as emp_name
					, c.task_id 
					, c.stamp
					, c.capex_ind 
					, c.efforts 
					, json_array(
							e.vv_2021_01, e.vv_2021_02, e.vv_2021_03, e.vv_2021_04, e.vv_2021_05, e.vv_2021_06
						  , e.vv_2021_07, e.vv_2021_08, e.vv_2021_09, e.vv_2021_10, e.vv_2021_11, e.vv_2021_12) as e_a
					, e.emp_total
					, json_array(
							t.vv_2021_01, t.vv_2021_02, t.vv_2021_03, t.vv_2021_04, t.vv_2021_05, t.vv_2021_06
						  , t.vv_2021_07, t.vv_2021_08, t.vv_2021_09, t.vv_2021_10, t.vv_2021_11, t.vv_2021_12) as t_a
					, t.duration 
				FROM jira_category_2021_01_01 c 
					left join jira_timeline_2021_01_01 t on (t.issue_key = c.task_id)
					left join jira_gusto jg on (jg.jira_emp_name = c.emp_name)
					left join employee_participation_2021_01_01 e on (jg.gusto_emp_name = e.emp_name)
		) w cross join generate_series m
	) x
	group by 1, 2, 3
) d
