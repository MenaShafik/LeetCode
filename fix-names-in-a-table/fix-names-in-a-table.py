# ================================================================
# Problem : Fix Names in a Table
# URL     : https://leetcode.com/problems/fix-names-in-a-table/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 60.6%
# Likes           : 1084
# Dislikes        : 143
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 809  (beats 95.53019999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761403777
#
# --- Hints ---
# N/A
# ================================================================

SELECT 
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)), 
        LOWER(SUBSTRING(name, 2, LEN(name)))
    ) AS name  
FROM users
ORDER BY user_id;

