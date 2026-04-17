# ================================================================
# Problem : Calculate Special Bonus
# URL     : https://leetcode.com/problems/calculate-special-bonus/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 57.0%
# Likes           : 1189
# Dislikes        : 83
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 548  (beats 83.03579999999995%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764444579
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT employee_id,
CASE WHEN
 employee_id % 2 != 0
and name NOT LIKE 'M%'
THEN salary
ELSE 0
END AS bonus 
FROM employees
order by employee_id
