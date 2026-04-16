# ================================================================
# Problem : Seasonal Sales Analysis
# URL     : https://leetcode.com/problems/seasonal-sales-analysis/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 62.0%
# Likes           : 66
# Dislikes        : 4
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 351  (beats 87.30160000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764715279
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
with category as (
SELECT 
CASE WHEN MONTH(S.sale_date) IN (12,1,2) THEN 'Winter'
WHEN MONTH(S.sale_date) IN (3,4,5) THEN 'Spring'
WHEN MONTH(S.sale_date) IN (6,7,8) THEN 'Summer'
ELSE 'Fall'
END AS season,
P.category,
SUM(S.quantity) AS
total_quantity,
SUM(S.quantity * S.price) as total_revenue
FROM products AS P
JOIN sales AS S
ON P.product_id = S.product_id 
group by CASE WHEN MONTH(S.sale_date) IN (12,1,2) THEN 'Winter'
WHEN MONTH(S.sale_date) IN (3,4,5) THEN 'Spring'
WHEN MONTH(S.sale_date) IN (6,7,8) THEN 'Summer'
ELSE 'Fall'
END ,p.category
),
ranked as (
    select
    season,
    category,
    total_quantity,
    total_revenue,
    row_number()over(partition by season order by total_quantity desc,total_revenue desc)
 as rn
from category
)
SELECT 
 season,
    category,
    total_quantity,
    total_revenue
    FROM ranked
    WHERE rn = 1
