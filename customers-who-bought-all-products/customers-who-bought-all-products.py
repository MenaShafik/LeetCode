# ================================================================
# Problem : Customers Who Bought All Products
# URL     : https://leetcode.com/problems/customers-who-bought-all-products/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 63.9%
# Likes           : 1160
# Dislikes        : 98
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1441  (beats 30.155500000000476%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760538161
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select customer_id 
from Customer as a
left join Product as b
on a.product_key = b.product_key 
group by customer_id
having count(distinct a.product_key) =
(
select
count(product_key)
 from product
 )
