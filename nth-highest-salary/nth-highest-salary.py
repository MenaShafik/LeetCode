# ================================================================
# Problem : Nth Highest Salary
# URL     : https://leetcode.com/problems/nth-highest-salary/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 39.0%
# Likes           : 2316
# Dislikes        : 1123
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 369  (beats 86.74780000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764188188
#
# --- Hints ---
# N/A
# ================================================================

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
SELECT DISTINCT salary
FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
FROM Employee) AS ranked_salaries
WHERE rank = @N
    );
END
