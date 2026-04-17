# ================================================================
# Problem : Movie Rating
# URL     : https://leetcode.com/problems/movie-rating/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 43.2%
# Likes           : 1005
# Dislikes        : 242
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 402  (beats 98.04139999999998%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761568347
#
# --- Hints ---
# N/A
# ================================================================

WITH combine_data AS (
    SELECT 
        mr.*,
        m.title,
        u.name
    FROM MovieRating AS mr
    JOIN Movies AS m
        ON mr.movie_id = m.movie_id  
    JOIN Users AS u 
        ON mr.user_id = u.user_id  
)
SELECT results
FROM (
    SELECT TOP 1
            name AS results
    FROM combine_data
    GROUP BY name
    ORDER BY COUNT(*) DESC, name ASC

    UNION ALL

    SELECT TOP 1
            title AS results
    FROM combine_data
    WHERE created_at >= '2020-02-01' AND created_at <= '2020-02-29'
    GROUP BY title
    ORDER BY AVG(rating * 1.0) DESC, title ASC
) x
