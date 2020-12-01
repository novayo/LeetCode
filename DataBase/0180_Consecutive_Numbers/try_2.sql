/* Write your PL/SQL query statement below */
select distinct
    Num as ConsecutiveNums
from
(
    select
        lag(Num) over(order by Id) prev,
        Num,
        lead(Num) over(order by Id) "Next"
    from
        Logs
) tmp
where 
    prev = Num
    and "Next" = Num
