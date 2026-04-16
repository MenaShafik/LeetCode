# ================================================================
# Problem : Big Countries
# URL     : https://leetcode.com/problems/big-countries/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 68.4%
# Likes           : 3382
# Dislikes        : 1382
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 505  (beats 97.90950000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759783275
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
name,
population, 
area
FROM World 
where population >= 25000000
 or
area >= 3000000   
