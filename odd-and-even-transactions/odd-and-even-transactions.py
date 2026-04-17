# ================================================================
# Problem : Odd and Even Transactions
# URL     : https://leetcode.com/problems/odd-and-even-transactions/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 68.2%
# Likes           : 72
# Dislikes        : 39
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 253  (beats 90.5108%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764619519
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT transaction_date,
SUM(odd) AS odd_sum,
SUM(even) AS even_sum
FROM (
    SELECT transaction_date,
CASE WHEN amount % 2 = 1 THEN amount
ELSE 0
END AS odd,
CASE WHEN amount % 2 = 0 THEN amount
ELSE 0 END AS even
    FROM transactions

)T
    GROUP BY transaction_date
    ORDER BY transaction_date
