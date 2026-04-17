# ================================================================
# Problem : Article Views I
# URL     : https://leetcode.com/problems/article-views-i/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 76.7%
# Likes           : 2289
# Dislikes        : 144
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 738  (beats 94.91800000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759783755
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT DISTINCT viewer_id AS id
FROM Views AS V
WHERE V.author_id  = V.viewer_id 
ORDER BY V.viewer_id ASC
