# ================================================================
# Problem : User Activity for the Past 30 Days I
# URL     : https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 50.7%
# Likes           : 1098
# Dislikes        : 1025
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1072  (beats 18.59070000000016%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761054788
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select activity_date as day,
count(DISTINCT user_id) as active_users 
from Activity 
WHERE activity_date BETWEEN DATEADD(DAY, -29, '2019-07-27') AND '2019-07-27'
group by activity_date
