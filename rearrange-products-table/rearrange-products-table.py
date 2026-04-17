# ================================================================
# Problem : Rearrange Products Table
# URL     : https://leetcode.com/problems/rearrange-products-table/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 85.5%
# Likes           : 978
# Dislikes        : 68
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 373  (beats 67.43439999999995%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764426409
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select p1.product_id,
'store1' as store,
p1.store1 as price 
from products as p1
where p1.store1 is not null
union 
select p2.product_id,
'store2' as store,
p2.store2 as price 
from products as p2
where p2.store2 is not null
union
select p3.product_id,
'store3' as store,
p3.store3 as price 
from products as p3
where p3.store3 is not null
order by store
