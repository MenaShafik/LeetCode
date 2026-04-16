# ================================================================
# Problem : Group Sold Products By The Date
# URL     : https://leetcode.com/problems/group-sold-products-by-the-date/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 77.9%
# Likes           : 1719
# Dislikes        : 127
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 420  (beats 76.7574%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761776759
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
SELECT 
sell_date  ,
COUNT(DISTINCT product) AS  num_sold,
group_concat(DISTINCT product) AS products
FROM activities
GROUP BY sell_date;
