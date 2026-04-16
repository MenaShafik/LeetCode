# ================================================================
# Problem : Invalid Tweets
# URL     : https://leetcode.com/problems/invalid-tweets/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 85.2%
# Likes           : 1498
# Dislikes        : 381
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 773  (beats 76.21049999999991%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759784432
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT distinct
tweet_id 
FROM Tweets 
where len(content) > 15
