/* Write your PL/SQL query statement below */
select
    w1.id
from
    Weather w1
left join 
    Weather w2
on 
    w1.recordDate = w2.recordDate + 1
where
    w1.Temperature > w2.Temperature