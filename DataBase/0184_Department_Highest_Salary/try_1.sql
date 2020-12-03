/* Write your PL/SQL query statement below */

select
    bb.Name as Department,
    aa.Name as Employee,
    Salary
from
(
select
    Name,
    Salary,
    DepartmentId as Id,
    rank() over(partition by departmentid order by salary desc) as rn
from
    Employee
) aa
inner join
    Department bb
on
    aa.Id = bb.Id
where
    aa.rn = 1