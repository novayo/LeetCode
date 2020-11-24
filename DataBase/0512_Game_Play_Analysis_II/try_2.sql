/* Write your PL/SQL query statement below */
select
    player_id,
    device_id
from
(
    select
        player_id,
        device_id,
        row_number() over (partition by player_id order by event_date asc) as rn
    from
        Activity
)
where
    rn = 1;