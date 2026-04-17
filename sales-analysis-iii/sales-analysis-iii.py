# ================================================================
# Problem : Sales Analysis III
# URL     : https://leetcode.com/problems/sales-analysis-iii/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 47.5%
# Likes           : 863
# Dislikes        : 170
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 2446  (beats 49.697699999999884%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764077216
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT DISTINCT S.product_id ,
P.product_name 
FROM sales AS S 
LEFT JOIN product AS P
ON S.product_id  = P.product_id 
WHERE S.sale_date BETWEEN '2019-01-01' AND '2019-03-31' AND P.product_id not in (
    select distinct product_id from Sales where sale_date > '2019-03-31' or sale_date < '2019-01-01'
)
