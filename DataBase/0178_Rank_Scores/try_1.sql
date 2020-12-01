/* Write your PL/SQL query statement below */
select
    Score as score,
    dense_rank() over(order by score desc) as Rank
from
    Scores