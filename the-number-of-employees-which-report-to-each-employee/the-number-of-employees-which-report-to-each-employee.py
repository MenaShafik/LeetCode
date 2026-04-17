# ================================================================
# Problem : The Number of Employees Which Report to Each Employee
# URL     : https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 53.2%
# Likes           : 898
# Dislikes        : 110
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 719  (beats 52.47589999999989%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760360284
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
    e.employee_id,
    e.name,
    COUNT(r.employee_id) AS reports_count,
   round( AVG(r.age *1.0),0) AS average_age
FROM Employees AS e
LEFT JOIN Employees AS r
    ON r.reports_to = e.employee_id
GROUP BY e.employee_id, e.name
HAVING COUNT(r.employee_id) > 0
ORDER BY e.employee_id;

