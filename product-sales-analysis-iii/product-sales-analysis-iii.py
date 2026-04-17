# ================================================================
# Problem : Product Sales Analysis III
# URL     : https://leetcode.com/problems/product-sales-analysis-iii/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 45.9%
# Likes           : 789
# Dislikes        : 1131
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1932  (beats 97.57120000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761149171
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select  product_id,
year as first_year,
quantity,
price
from (
    select *,
    rank()over(partition by product_id order by year) as r
    from Sales
)t
where r = 1
