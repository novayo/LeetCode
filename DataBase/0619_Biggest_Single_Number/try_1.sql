/* Write your PL/SQL query statement below */
select
    max(num) as num
from(
    select
        num
    from
        my_numbers
    group by num
    having count(num) = 1
)