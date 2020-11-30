/* Write your PL/SQL query statement below */
with sorted as(
    select
        x,
        x - lag(x) over(order by x) as diff
    from
        point
)
select
    min(diff) as shortest
from
    sorted
;