# ================================================================
# Problem : Employees With Missing Information
# URL     : https://leetcode.com/problems/employees-with-missing-information/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 73.1%
# Likes           : 796
# Dislikes        : 41
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 341  (beats 85.95030000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764194190
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT employee_id 
FROM salaries
WHERE employee_id NOT IN(
SELECT employee_id 
FROM Employees
)
UNION 
SELECT employee_id 
FROM Employees
WHERE employee_id NOT IN(
SELECT employee_id 
FROM salaries
)
