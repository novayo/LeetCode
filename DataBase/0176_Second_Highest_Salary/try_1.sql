/* Write your PL/SQL query statement below */
with tmp as
(
    select
        Salary,
        dense_rank() over (order by Salary desc) as rank
    from
        Employee
)

select
    MAX(
        case when
            rank=2
        then
            Salary
        else
            null
        end
    )
    as
        SecondHighestSalary
from
    tmp
