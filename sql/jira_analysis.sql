
select *
	, round(cast(cnt as float) / cnt_total, 2) as sov
	, round(cast(issue_cnt as float) / issue_total, 2) as issue_sov
from (
	select (items_len)
		, count(1) cnt
		, count(distinct issue_id) as issue_cnt
		, sum(count(1)) over() as cnt_total
		, sum(count(distinct issue_id)) over() as issue_total
	from jira_changelog jc 
	group by 1
	order by 1
)

select capex_ind
    , is_support
	, ct_no_capex
	, ifnull(task_category, 'abczgucb') = 'Not Classified to CapEx Category' as not_classifed
	, count(1) cnt
	, sum(count(1)) over() as total_cnt
from jira_category_2021_01_01
group by 1, 2, 3


select *
from jira_category_2021_01_01
where capex_ind < 0

update jira_category_2021_01_01 set capex_ind = 0 where task_id = 'ILV-4871'


select *
from jira_category_2021_01_01
where task_id = 'BAC-5130'

select stamp
	, capex_ind
	, count(1) cnt
	, sum(count(1)) over(PARTITION by capex_ind) as group_cnt
from jira_category_2020_01_01
group by 1, 2

capex_ind|is_support|ct_no_capex|not_classifed|cnt|total_cnt|
---------+----------+-----------+-------------+---+---------+
      0.0|No        |           |            1|636|     2625|
      0.0|No        |        1.0|            0|621|     2625|
      0.0|Yes       |           |            1|544|     2625|
      0.0|Yes       |        1.0|            0| 30|     2625|
      1.0|No        |           |            0|794|     2625|

select *
from jira_category_2020_01_01
where capex_ind not in (0,1)

select * 
from jira_timeline_2021_01_01 jt 
where  vv_2021_01 > 30
	or vv_2021_02 > 30 
	or vv_2021_03 > 30 
	or vv_2021_04 > 30 
	or vv_2021_05 > 30 
	or vv_2021_06 > 30 
	or vv_2021_07 > 30 
	or vv_2021_08 > 30 
	or vv_2021_09 > 30 
	or vv_2021_10 > 30 
	or vv_2021_11 > 30 
	or vv_2021_11 > 30 
	
select project_key, count(1)
from jira_issues  jil 
group by 1


select *
from jira_issue_lifecycle
where issue_key in ('ILV-4069', 'ILV-4123')

	, round(sum(sum(efforts * t_m / duration)) over(partition by emp_name, month_date), 2) as efforts_month
	, round(sum(sum(efforts * t_m / duration)) over(partition by emp_name), 2) as efforts_year


select emp_name
	, month_date
	, stamp
	, max(emp_total) as emp_contrib
	, round(max(e_m / emp_total), 2) as w2_fraction
	, round(sum(efforts * t_m / duration), 2) as efforts_category
from (
	select *
		, IFNULL(json_extract(e_a,'$['||month_num||']'),0) as e_m
		, IFNULL(json_extract(t_a,'$['||month_num||']'),0) as t_m
	from (
		WITH RECURSIVE
		  month_gen(x) AS (
		     SELECT 0
		     UNION ALL
		     SELECT x+1 FROM month_gen
		      LIMIT (SELECT ROUND(((julianday('2020-12-01') - julianday('2020-01-01'))/30) + 1))
		  )
		SELECT date(julianday('2020-01-01'), '+' || x || ' month') as month_date
			, x as month_num
			, c.emp_name 
			, c.task_id 
			, c.stamp
			, c.capex_ind 
			, c.efforts 
			, json_array(
					e.vv_2020_01, e.vv_2020_02, e.vv_2020_03, e.vv_2020_04, e.vv_2020_05, e.vv_2020_06
				  , e.vv_2020_07, e.vv_2020_08, e.vv_2020_09, e.vv_2020_10, e.vv_2020_11, e.vv_2020_12) as e_a
			, e.emp_total
			, json_array(
					t.vv_2020_01, t.vv_2020_02, t.vv_2020_03, t.vv_2020_04, t.vv_2020_05, t.vv_2020_06
				  , t.vv_2020_07, t.vv_2020_08, t.vv_2020_09, t.vv_2020_10, t.vv_2020_11, t.vv_2020_12) as t_a
			, t.duration 
		FROM month_gen 
			cross join jira_category_2020_01_01 c 
			left join jira_timeline_2020_01_01 t on (t.issue_key = c.task_id)
			left join jira_gusto jg on (jg.jira_emp_name = c.emp_name)
			left join employee_participation_2020_01_01 e  on (jg.gusto_emp_name = e.emp_name)
		group by 1, 2, 3, 4, 5, 6
	) 
)
group by 1, 2, 3



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
				SELECT COALESCE(c.emp_name, c.emp_name) as emp_name
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


with recursive generate_series(value) AS (
  select 0
  union all
  select value + 1 from generate_series
  where value + 1 <= 11
)
select emp_name
		, month_date
	from (
		select m.value as month_num
			, date(julianday('2020-01-01'), '+' || m.value || ' month') as month_date
			, w.*
			, IFNULL(json_extract(e_a,'$['||m.value||']'),0) as e_m
			, IFNULL(json_extract(t_a,'$['||m.value||']'),0) as t_m
		from (
				SELECT c.emp_name 
					, c.task_id 
					, c.stamp
					, c.capex_ind 
					, c.efforts 
					, json_array(
							e.vv_2020_01, e.vv_2020_02, e.vv_2020_03, e.vv_2020_04, e.vv_2020_05, e.vv_2020_06
						  , e.vv_2020_07, e.vv_2020_08, e.vv_2020_09, e.vv_2020_10, e.vv_2020_11, e.vv_2020_12) as e_a
					, e.emp_total
					, json_array(
							t.vv_2020_01, t.vv_2020_02, t.vv_2020_03, t.vv_2020_04, t.vv_2020_05, t.vv_2020_06
						  , t.vv_2020_07, t.vv_2020_08, t.vv_2020_09, t.vv_2020_10, t.vv_2020_11, t.vv_2020_12) as t_a
					, t.duration 
				FROM jira_category_2020_01_01 c 
					left join jira_timeline_2020_01_01 t on (t.issue_key = c.task_id)
					left join jira_gusto jg on (jg.jira_emp_name = c.emp_name)
					left join employee_participation_2020_01_01 e  on (jg.gusto_emp_name = e.emp_name)
		) w cross join generate_series m
	) 
	group by 1, 2







	
select c.emp_name as jira , e.emp_name as gusto, count(1)
from jira_category_2020_01_01 c 
	left join jira_gusto jg on (jg.jira_emp_name = c.emp_name)
	left join employee_participation_2020_01_01 e  on (jg.gusto_emp_name = e.emp_name)
group by 1, 2

select c.emp_name as jira, count(1)
from jira_category_2021_01_01 c
group by 1


delete from jira_changelog where issue_id  in (
	select ji.id, max_date, status_change_date, updated_date
	from jira_issues ji left join (
		select issue_id, max(created_date) as max_date
		from jira_changelog jc 
		group by 1
	) d on (d.issue_id = ji.id)
	where status_change_date > max_date or updated_date > max_date 
)

select  max(created_date)
from jira_issues ji   
limit 100

select *
from jira_gusto jg 

select max(created_date)
from jira_changelog jc 

select *
from jira_issue_lifecycle jil 


select *
from employee_participation_2020_01_01


drop table jira_timeline


select max(created_date)
from jira_issues ji 


select issue_created, count(1)
from jira_issue_lifecycle
group by 1
order by 1 asc

select DATE('2022-10-02','+1 year')

WITH RECURSIVE dates(x) AS ( 
            SELECT '2015-01-01' 
                UNION ALL 
            SELECT DATE(x, '+1 MONTHS') FROM dates WHERE x<'2016-01-01' 
        ) 
        SELECT * FROM dates;


select * from jira_changelog 



select count(1) from jira_issues ji 

select status_name_from, status_name_to, count(1)
from jira_status js 
group by 1, 2
order by 3 desc


select count(1), count(distinct issue_id)
from jira_status js 

select COALESCE(workflow, status_name) as wf
	, sum(case when workflow like '%In Progress%' then 1 else 0 end) as in_progress
	, count(1) as cnt
	, sum(count(1)) over() as total
from (
	select id,  ji.created_date, ji.status_name, ji.updated_date, ji.status_change_date , workflow
	from jira_issues ji left join (
		select issue_id, group_concat(status_name_from||'->'||status_name_to , ',') as workflow
		from jira_status js 
		group by 1
	) s on (s.issue_id = ji.id)
)
--where workflow not like '%In Progres%'
group by 1
order by 3 desc



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
	where status_name not in ('Won''t Do') 
		and resolution_name not in ('Won''t Do', 'Duplicate')
	order by 1, 2
) d
group by 1, 2


delete from jira_issue_lifecycle

select JULIANDAY(end_date) - JULIANDAY(start_date) + 1 as duration, *
from (
	select COALESCE(work_started, issue_started, issue_created) as start_date
		,  COALESCE(work_ended, issue_completed) as end_date
		, ji.*
	from jira_issue_lifecycle  ji
) d
order by 1 desc

select status_name_to, 1, count(1)
from jira_status js 
group by 1, 2



select '{ ''status'': "'||ifnull(status_name, 'None')||
	'", ''resolution_name'': "'||ifnull(resolution_name, 'None')||
	'", ''resolution_description'': "'||ifnull(resolution_description, 'None')||'"},' as json, count(1) as cnt
from jira_issues ji 
group by 1
order by 2 desc

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
							

select 'map_'||lower(project_key), count(1), max(created_date)
from jira_issues ji 
group by 1

SELECT assignee_email, assignee_name, created_date  , *
FROM jira_issues
WHERE "key" like 'TWR%'
	and assignee_name = 'Noelle Laureano'

	
select *
from jira_nord_terms jnt 
	
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
			, ji.parent_key as project_id
			, ji.parent_summary  as project_desc
			, jo.capex_category 
			, jo.project_driver 
			, case when inprogress_date is not null and inprogress_date > st.start_date then inprogress_date else start_date end as start_date
			, case when closed_date is not null and closed_date < end_date then closed_date else end_date end as end_date  
			, ji.created_date  
			, ji.updated_date 
			, ji.status_change_date 
			, ji.status_name 
			, ji.resolution_name 
			, (select count(1) from jira_nord_terms  where instr( lower(ji.summary), term) > 0) as terms_cnt
			, (select count(1) from jira_support_issues where ji."key" = issue_key) as exclude_cnt
		from jira_issues ji 
			left join jira_ol jo on (jo.id = ji.parent_id)
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
						and created_date < '2022-05-01'
	

