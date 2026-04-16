# ================================================================
# Problem : Count Salary Categories
# URL     : https://leetcode.com/problems/count-salary-categories/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 64.3%
# Likes           : 741
# Dislikes        : 115
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 10258  (beats 84.58750000000038%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761512692
#
# --- Hints ---
# N/A
# ================================================================

WITH Categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)
SELECT 
    c.category,
    COALESCE(COUNT(t.account_id), 0) AS accounts_count
FROM Categories AS c
LEFT JOIN (
    SELECT 
        account_id,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category
    FROM Accounts
) AS t
    ON c.category = t.category
GROUP BY c.category;

