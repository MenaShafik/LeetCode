# ================================================================
# Problem : Find Total Time Spent by Each Employee
# URL     : https://leetcode.com/problems/find-total-time-spent-by-each-employee/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 86.4%
# Likes           : 809
# Dislikes        : 25
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 348  (beats 84.83979999999998%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764426751
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT event_day  AS day,
emp_id,
sum(out_time -in_time) AS total_time 
FROM Employees
GROUP BY event_day,emp_id;
