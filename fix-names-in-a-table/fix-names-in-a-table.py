# ================================================================
# Problem : Fix Names in a Table
# URL     : https://leetcode.com/problems/fix-names-in-a-table/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 60.6%
# Likes           : 1085
# Dislikes        : 143
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 809  (beats 96.46440000000001%)
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

