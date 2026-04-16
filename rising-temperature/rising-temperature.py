# ================================================================
# Problem : Rising Temperature
# URL     : https://leetcode.com/problems/rising-temperature/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 51.2%
# Likes           : 4256
# Dislikes        : 745
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1222  (beats 5.009400000000016%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759837473
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
w1.id
FROM Weather w1
JOIN Weather w2
ON DATEDIFF(DAY, w2.recordDate, w1.recordDate) = 1  
WHERE w1.temperature > w2.temperature;



