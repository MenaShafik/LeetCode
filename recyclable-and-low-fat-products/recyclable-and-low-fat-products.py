# ================================================================
# Problem : Recyclable and Low Fat Products
# URL     : https://leetcode.com/problems/recyclable-and-low-fat-products/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 88.7%
# Likes           : 3364
# Dislikes        : 132
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 395  (beats 85.18119999999998%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759702326
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select product_id
from products 
where low_fats = recyclable and recyclable != 'N'
