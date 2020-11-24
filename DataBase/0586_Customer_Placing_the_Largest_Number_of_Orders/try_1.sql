/* Write your PL/SQL query statement below */
select
    customer_number
from
(
    select
        customer_number,
        count(*) as num
    from
        orders
    group by
        customer_number
    order by num desc
)
where
    rownum=1