# ================================================================
# Problem : List the Products Ordered in a Period
# URL     : https://leetcode.com/problems/list-the-products-ordered-in-a-period/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 71.7%
# Likes           : 584
# Dislikes        : 48
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 349  (beats 83.85359999999999%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761777640
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT
P.product_name,
SUM(O.unit) AS unit    
FROM Products AS P
LEFT JOIN Orders AS O
ON P.product_id  = O.product_id  
WHERE order_date  BETWEEN '2020-02-1' AND'2020-2-29'
GROUP BY P.product_name
having SUM(O.unit)>=100
ORDER BY SUM(O.unit) DESC

