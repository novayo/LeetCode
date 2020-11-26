/* Write your PL/SQL query statement below */
with A as (
    select count(*) as a from (select distinct requester_id, accepter_id from request_accepted)
)
,
B as (
    select count(*) as b from (select distinct sender_id, send_to_id from friend_request)
)

select
    case when b=0 then 0
         else round(a/b, 2)
    end as accept_rate
from A, B;