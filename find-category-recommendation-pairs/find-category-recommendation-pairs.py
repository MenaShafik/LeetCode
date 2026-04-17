# ================================================================
# Problem : Find Category Recommendation Pairs
# URL     : https://leetcode.com/problems/find-category-recommendation-pairs/
# Difficulty : Hard
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 63.0%
# Likes           : 35
# Dislikes        : 6
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 567  (beats 91.36509999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766847015
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
with cte as (
    select user_id,
    pp.product_id ,
    category,
    price,quantity  
        from ProductPurchases  as pp
    left join ProductInfo as pi
    on pp.product_id = pi.product_id 
    order by user_id
)
,cte2 as (
    select a.user_id,
    a.category c1 ,
     b.category c2 ,
     a.price,
     count(*) as c
      from cte a
      join cte b
      on a.category< b.category and a.user_id=b.user_id
      group by 1,2,3
       order by 2,3
)
select c1 category1 ,
 c2 category2 ,
  count(*) customer_count
   from cte2
    group by c1,c2
    having count(*)>=3
    order by count(*) desc,c1,c2
