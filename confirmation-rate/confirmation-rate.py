# ================================================================
# Problem : Confirmation Rate
# URL     : https://leetcode.com/problems/confirmation-rate/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 61.8%
# Likes           : 1588
# Dislikes        : 133
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 415  (beats 94.12579999999998%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760818854
#
# --- Hints ---
# N/A
# ================================================================

SELECT S.user_id ,
ROUND(CAST(SUM(CASE WHEN C.action='confirmed' THEN 1 ELSE 0 END) AS FLOAT)/count(s.user_id),2) AS confirmation_rate 
FROM Signups AS S
LEFT JOIN Confirmations AS C
ON S.user_id = C.user_id 
GROUP BY S.user_id 
ORDER BY confirmation_rate
