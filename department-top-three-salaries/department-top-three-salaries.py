# ================================================================
# Problem : Department Top Three Salaries
# URL     : https://leetcode.com/problems/department-top-three-salaries/
# Difficulty : Hard
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 60.2%
# Likes           : 2602
# Dislikes        : 282
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 431  (beats 78.3666%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761081810
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT Department,
Employee,
salary 
FROM (
SELECT D.name AS Department,
E.name  AS Employee,
E.salary AS salary,
Dense_rank()OVER(partition by E.departmentId  ORDER BY E.salary DESC) AS RANK_OF_MINA
FROM Employee AS E
JOIN Department AS D
ON E.departmentId = D.id 
) AS RANKED
WHERE RANK_OF_MINA <=3
