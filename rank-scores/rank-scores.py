# ================================================================
# Problem : Rank Scores
# URL     : https://leetcode.com/problems/rank-scores/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 67.5%
# Likes           : 2502
# Dislikes        : 304
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 353  (beats 62.80310000000005%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760709639
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT score ,
DENSE_RANK() OVER(ORDER BY score DESC) AS rank 
FROM Scores 
