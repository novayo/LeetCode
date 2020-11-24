/* Write your PL/SQL query statement below */
select
  Name as Customers
from
    Customers
where
    id not in (select customerid from orders)