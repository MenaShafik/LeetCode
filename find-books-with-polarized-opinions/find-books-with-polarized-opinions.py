# ================================================================
# Problem : Find Books with Polarized Opinions
# URL     : https://leetcode.com/problems/find-books-with-polarized-opinions/
# Difficulty : Medium
# Category   : Database
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 42.2%
# Likes           : 52
# Dislikes        : 12
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 496  (beats 99.61559999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766494387
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
WITH A AS (
    SELECT 
        C.book_id,
        C.title,
        C.author,
        C.genre,
        C.pages,
        MAX(B.session_rating) - MIN(B.session_rating) AS rating_spread,
        ROUND(SUM(CASE WHEN B.session_rating >= 4 OR B.session_rating <= 2 THEN 1 ELSE 0 END) / COUNT(B.session_id), 2) AS polarization_score
    FROM reading_sessions B
    JOIN books C
        ON B.book_id = C.book_id
    GROUP BY 
        C.book_id,
        C.title,
        C.author,
        C.genre,
        C.pages
    HAVING 
        COUNT(B.session_id) >= 5
        AND MAX(B.session_rating) >= 4
        AND MIN(B.session_rating) <= 2
        AND SUM(CASE WHEN B.session_rating >= 4 OR B.session_rating <= 2 THEN 1 ELSE 0 END) / COUNT(B.session_id) >= 0.6
)
SELECT *
FROM A
ORDER BY polarization_score DESC, title DESC;

