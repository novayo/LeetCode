/* Write your PL/SQL query statement below */
select c2.seat_id from cinema c1 inner join cinema c2 on c1.seat_id + 1 = c2.seat_id and c1.free=1 and c2.free=1
union
select c1.seat_id from cinema c1 inner join cinema c2 on c1.seat_id + 1 = c2.seat_id and c1.free=1 and c2.free=1
