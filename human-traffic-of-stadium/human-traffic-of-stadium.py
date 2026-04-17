# ================================================================
# Problem : Human Traffic of Stadium
# URL     : https://leetcode.com/problems/human-traffic-of-stadium/
# Difficulty : Hard
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 51.1%
# Likes           : 853
# Dislikes        : 577
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 333  (beats 93.12389999999999%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1767438258
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below

with cte 
as (
    select*,id-row_number() over(order by id) as diff
    from stadium
    where people >= 100
)
select id,
visit_date,
people
from cte
where diff  in (select diff from cte group by diff having count(*) >=3)

