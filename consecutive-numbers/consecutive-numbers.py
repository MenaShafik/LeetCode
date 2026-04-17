# ================================================================
# Problem : Consecutive Numbers
# URL     : https://leetcode.com/problems/consecutive-numbers/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 48.2%
# Likes           : 2742
# Dislikes        : 363
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 559  (beats 47.28360000000005%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760964702
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT DISTINCT L1.num AS ConsecutiveNums 
FROM Logs AS L1,Logs AS L2,Logs AS L3
WHERE L1.id = L2.id - 1
AND L2.id = L3.id - 1
AND L1.num = L2.num
AND L2.num = L3.num
