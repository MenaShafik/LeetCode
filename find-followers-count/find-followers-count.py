# ================================================================
# Problem : Find Followers Count
# URL     : https://leetcode.com/problems/find-followers-count/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 69.6%
# Likes           : 760
# Dislikes        : 49
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 801  (beats 11.122599999999956%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760537499
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select user_id,
count(follower_id ) as followers_count
from Followers 
group by user_id
