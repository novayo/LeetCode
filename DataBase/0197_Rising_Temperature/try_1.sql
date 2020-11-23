/* Write your PL/SQL query statement below */
select
    w1.id
from
    Weather w1, Weather w2
where
    w1.recordDate = w2.recordDate + 1 and
    w1.Temperature > w2.Temperature