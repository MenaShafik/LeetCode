# ================================================================
# Problem : Analyze Subscription Conversion 
# URL     : https://leetcode.com/problems/analyze-subscription-conversion/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 74.2%
# Likes           : 70
# Dislikes        : 6
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 288  (beats 81.3924%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1765402049
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
with cte as ( 
    select 
    user_id,
    activity_type ,
     avg(case when activity_type  = 'free_trial' then activity_duration else 0 end)
  as  trial_avg_duration ,
    avg(case when activity_type  = 'paid' then activity_duration else 0 end) as paid_avg_duration 
    from UserActivity
    group by user_id,activity_type 
)
select user_id,
round(sum(trial_avg_duration),2) as trial_avg_duration,
round(sum(paid_avg_duration),2) as paid_avg_duration
from cte
group by user_id
having sum(paid_avg_duration) >0
order by user_id
