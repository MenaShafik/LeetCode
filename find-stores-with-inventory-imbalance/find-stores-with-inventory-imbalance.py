# ================================================================
# Problem : Find Stores with Inventory Imbalance
# URL     : https://leetcode.com/problems/find-stores-with-inventory-imbalance/
# Difficulty : Medium
# Category   : Database
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 47.9%
# Likes           : 47
# Dislikes        : 9
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 470  (beats 98.12270000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1765975709
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
/* Write your T-SQL query statement below */
WITH MM AS (
SELECT I.store_id,
S.store_name,
S.location,
product_name,
quantity,
price,
first_value(product_name)over(partition by I.store_id order by price desc)
AS most_exp_product,

first_value(quantity) over(partition by I.store_id order by price desc)
as expen_pro_quantity,

first_value(product_name)over(partition by I.store_id order by price)
AS cheapest_product,
first_value(quantity) over(partition by I.store_id order by price)
as cheap_pro_quantity,
row_number()over(partition by I.store_id) as rnk
FROM inventory AS I
JOIN stores AS S
ON I.store_id = S.store_id 
)
SELECT store_id,
store_name,
location,
most_exp_product,
cheapest_product,
ROUND((cheap_pro_quantity/expen_pro_quantity),2) AS imbalance_ratio
FROM MM
WHERE RNK = 1 AND expen_pro_quantity < cheap_pro_quantity AND store_id IN (
    select i.store_id
from stores s
join inventory i
on s.store_id = i.store_id
group by 1
having count(distinct product_name) >= 3 )
order by (cheap_pro_quantity/expen_pro_quantity) desc ,store_name 
