/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with t1 as (
select distinct submission_date from submissions order by submission_date)
,mapping_table as (select submission_date, hacker_id from t1
cross join (select hacker_id from hackers) t2) -- create mapping table with all hacker_id
,sub as (select distinct submission_date, hacker_id from submissions)
,daily as (select t1.submission_date, t1.hacker_id,
avg(case when t2.hacker_id is null then 0 else 1 end) over (partition by t1.hacker_id order by t1.submission_date) avg1
from mapping_table t1
left join sub t2
on t1.submission_date = t2.submission_date
and t1.hacker_id = t2.hacker_id)
,final_1 as(
select submission_date, sum(case when avg1 = 1 then 1 else 0 end) total from daily 
group by submission_date
order by submission_date)
,t3 as (select submission_date, hacker_id
            ,rank() over (partition by submission_date order by            count(submission_id) desc, hacker_id asc) rk
            from Submissions
            group by submission_date, hacker_id)
,final_2 as (select submission_date, t1.hacker_id, name from t3 t1
join hackers t2
    on t1.hacker_id = t2.hacker_id
where rk = 1)
select f1.submission_date, f1.total, f2.hacker_id, f2.name from final_1 f1
join final_2 f2
    on f1.submission_date = f2.submission_date;
