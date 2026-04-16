# ================================================================
# Problem : Project Employees I
# URL     : https://leetcode.com/problems/project-employees-i/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 66.7%
# Likes           : 1050
# Dislikes        : 206
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1339  (beats 19.18770000000015%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759956245
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT p.project_id,round(avg(E.experience_years* 1.0),2)  as average_years 
FROM Project AS p 
LEFT JOIN Employee AS E
ON p.employee_id = E.employee_id 
group by p.project_id
