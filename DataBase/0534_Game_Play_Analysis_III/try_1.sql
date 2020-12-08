/* Write your PL/SQL query statement below */
select
    player_id,
    substr(event_date, 1, 10) as event_date,
    sum(games_played) over(partition by player_id order by event_date) as games_played_so_far 
from
    Activity
;