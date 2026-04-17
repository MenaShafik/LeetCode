# ================================================================
# Problem : Last Person to Fit in the Bus
# URL     : https://leetcode.com/problems/last-person-to-fit-in-the-bus/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 69.2%
# Likes           : 1114
# Dislikes        : 51
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1087  (beats 74.30000000000008%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760965919
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select top(1) p.person_name
from (select person_name,
sum(Weight) over(order by turn)as rn
from Queue) p
where rn<=1000
order by rn desc
