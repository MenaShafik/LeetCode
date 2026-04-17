# ================================================================
# Problem : Immediate Food Delivery II
# URL     : https://leetcode.com/problems/immediate-food-delivery-ii/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 55.9%
# Likes           : 1267
# Dislikes        : 173
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 803  (beats 91.16029999999999%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761511267
#
# --- Hints ---
# N/A
# ================================================================

with f_order
as (
select customer_id , order_date,customer_pref_delivery_date cf_date,
rank() over(partition by customer_id order by order_date ) rnk
from delivery )
select
round(sum(case when order_date = cf_date then 1.0 else 0 end)
/count(order_date) * 100 ,2)
as "immediate_percentage"
from f_order where rnk <= 1
