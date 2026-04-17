# ================================================================
# Problem : Not Boring Movies
# URL     : https://leetcode.com/problems/not-boring-movies/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 75.1%
# Likes           : 1539
# Dislikes        : 565
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 253  (beats 65.79380000000005%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759873505
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT id,
movie,
description,
rating
FROM cinema
WHERE id %2 != 0 
and description  != 'boring'
order by rating desc
