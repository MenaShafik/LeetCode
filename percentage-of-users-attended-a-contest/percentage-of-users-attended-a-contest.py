# ================================================================
# Problem : Percentage of Users Attended a Contest
# URL     : https://leetcode.com/problems/percentage-of-users-attended-a-contest/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 60.2%
# Likes           : 1214
# Dislikes        : 109
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 2395  (beats 97.05880000000008%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760904802
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT R.contest_id ,
ROUND(CAST(COUNT(DISTINCT R.user_id) *100.0/ (SELECT DISTINCT count(U.user_id) FROM Users as U)AS FLOAT),2) AS percentage 
FROM Register AS R
GROUP BY R.contest_id
order by percentage desc,r.contest_id


