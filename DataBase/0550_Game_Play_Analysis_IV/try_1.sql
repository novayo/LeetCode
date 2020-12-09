/* Write your PL/SQL query statement below */
with a as (
    select 
        player_id,
        event_date
    from(
        select
            player_id,
            event_date,
            row_number() over(partition by player_id order by event_date asc) as rn
        from
            Activity
    )  
    where
        rn = 1
)
select
    round(count(b.player_id) / count(a.player_id), 2) as fraction
from
    a
left outer join
(
    select
        player_id,
        event_date
    from 
        Activity
) b
on
    a.player_id = b.player_id
    and a.event_date + 1 = b.event_date
;