# ================================================================
# Problem : Average Selling Price
# URL     : https://leetcode.com/problems/average-selling-price/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 37.2%
# Likes           : 1984
# Dislikes        : 271
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 288  (beats 98.48029999999999%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760353782
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
P.product_id,
ROUND(isnull(sum(US.units * P.price) * 1.0 / nullif(sum(US.units),0),0),2) as average_price 
from prices as P
left join UnitsSold as US 
on P.product_id = US.product_id
AND US.purchase_date BETWEEN P.start_date AND P.end_date
group by P.product_id
