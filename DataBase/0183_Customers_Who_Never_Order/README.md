Question: https://leetcode.com/problems/customers-who-never-order/

---

try_1.sql:
* Runtime: 736 ms, faster than 67.68% of Oracle online submissions for Customers Who Never Order.
* Memory Usage: 0B, less than 100.00% of Oracle online submissions for Customers Who Never Order.

> left outer join

---

try_2.sql:
* Runtime: 678 ms, faster than 92.93% of Oracle online submissions for Customers Who Never Order.
* Memory Usage: 0B, less than 100.00% of Oracle online submissions for Customers Who Never Order.

> sub query

> 用left join 會先join兩個table，若有很多個欄位會很耗時間，所以用sub query會快一些