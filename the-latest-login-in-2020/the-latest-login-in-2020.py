# ================================================================
# Problem : The Latest Login in 2020
# URL     : https://leetcode.com/problems/the-latest-login-in-2020/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 77.0%
# Likes           : 468
# Dislikes        : 20
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 780  (beats 93.93940000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764445371
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT user_id ,last_stamp          
FROM (
    SELECT user_id ,
    time_stamp AS last_stamp,
    ROW_NUMBER()OVER(PARTITION BY user_id ORDER BY time_stamp DESC) AS RNK
    FROM Logins 
    WHERE  YEAR(time_stamp) ='2020'
)T
WHERE RNK = 1
