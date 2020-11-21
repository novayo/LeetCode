/* Write your PL/SQL query statement below */
select
   Customers.Name as Customers
from
    Customers
left outer join
    Orders
on
    Customers.Id = Orders.CustomerId
where
    Orders.CustomerId is null