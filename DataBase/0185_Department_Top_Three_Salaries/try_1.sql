/* Write your PL/SQL query statement below */
select
 Department,
 Employee,
 Salary
from
(
select
    dense_rank() over(partition by DepartmentId order by Salary desc) rn,
    Department.Name as Department,
    Employee.Name as Employee,
    Employee.Salary as Salary
from
    Department
inner join
    Employee
on
    Department.id = Employee.Departmentid
) a
where
 a.rn < 4
