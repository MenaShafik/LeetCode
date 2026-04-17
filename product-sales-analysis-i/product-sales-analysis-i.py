# ================================================================
# Problem : Product Sales Analysis I
# URL     : https://leetcode.com/problems/product-sales-analysis-i/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 85.7%
# Likes           : 1482
# Dislikes        : 253
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 2767  (beats 68.43430000000009%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759827521
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT P.product_name,S.year,S.price
FROM Sales AS S
LEFT JOIN Product AS P
ON S.product_id = P.product_id
