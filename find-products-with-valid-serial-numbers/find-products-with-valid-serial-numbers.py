# ================================================================
# Problem : Find Products with Valid Serial Numbers
# URL     : https://leetcode.com/problems/find-products-with-valid-serial-numbers/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 30.3%
# Likes           : 57
# Dislikes        : 28
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 276  (beats 92.75360000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764596144
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT *
FROM products
WHERE description COLLATE Latin1_General_BIN2
      LIKE '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %'
OR description COLLATE Latin1_General_BIN2
      LIKE '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
OR description COLLATE Latin1_General_BIN2
      LIKE 'SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %'
OR description COLLATE Latin1_General_BIN2
      LIKE 'SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
ORDER BY product_id;
