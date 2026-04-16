# ================================================================
# Problem : Bank Account Summary II
# URL     : https://leetcode.com/problems/bank-account-summary-ii/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 83.0%
# Likes           : 548
# Dislikes        : 6
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 347  (beats 88.04890000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1763927731
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT *
FROM 
(SELECT DISTINCT U.name ,
SUM(T.amount)over(PARTITION BY T.account) AS
balance
FROM transactions AS T
LEFT JOIN users AS U
ON t.account = u.account)MINA
WHERE balance > 10000
