# ================================================================
# Problem : Exchange Seats
# URL     : https://leetcode.com/problems/exchange-seats/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 74.0%
# Likes           : 1909
# Dislikes        : 614
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 275  (beats 88.48860000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761232896
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
id,
CASE
WHEN id % 2 = 1 AND id + 1 IN (SELECT id FROM Seat)
THEN (SELECT student FROM Seat WHERE id = s.id + 1)
WHEN id % 2 = 0
THEN (SELECT student FROM Seat WHERE id = s.id - 1)
ELSE student
END AS student
FROM Seat s
ORDER BY id;
