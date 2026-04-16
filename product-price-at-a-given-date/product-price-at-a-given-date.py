# ================================================================
# Problem : Product Price at a Given Date
# URL     : https://leetcode.com/problems/product-price-at-a-given-date/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 57.8%
# Likes           : 1410
# Dislikes        : 335
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 842  (beats 76.57660000000007%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761150441
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT product_id,
price
FROM (
SELECT product_id,
new_price  AS price,
ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rnk
FROM Products 
WHERE  change_date <= '2019-08-16'
)t
WHERE t.rnk = 1
UNION
    SELECT product_id,
10 AS price
FROM products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'

