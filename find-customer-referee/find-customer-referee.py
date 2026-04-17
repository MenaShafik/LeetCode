# ================================================================
# Problem : Find Customer Referee
# URL     : https://leetcode.com/problems/find-customer-referee/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 72.8%
# Likes           : 2975
# Dislikes        : 413
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 528  (beats 36.41770000000004%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759704020
#
# --- Hints ---
# Be careful of the NULL value
# ================================================================

/* Write your T-SQL query statement below */
select name 
from customer
where referee_id !=2 or referee_id is null
