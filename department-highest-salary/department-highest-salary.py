# ================================================================
# Problem : Department Highest Salary
# URL     : https://leetcode.com/problems/department-highest-salary/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 57.8%
# Likes           : 2407
# Dislikes        : 212
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 491  (beats 24.78600000000004%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761167850
#
# --- Hints ---
# N/A
# ================================================================

SELECT 
D.name AS Department ,
E.name AS Employee ,
E.salary AS Salary 
FROM 
(
    SELECT E.*,
    RANK()OVER(PARTITION BY departmentId ORDER BY salary DESC) AS RNK
    FROM Employee AS E
)E
JOIN Department AS D
ON E.departmentId = D.id  
WHERE E.RNK = 1
