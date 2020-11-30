/* Write your PL/SQL query statement below */
with sorted as(
    select
        x,
        row_number() over(order by x) as rn
    from
        point
)
select
    min(a.x-b.x) as shortest
from
    sorted a, sorted b
where
    a.rn = b.rn + 1
;