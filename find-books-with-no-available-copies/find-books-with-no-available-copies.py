# ================================================================
# Problem : Find Books with No Available Copies
# URL     : https://leetcode.com/problems/find-books-with-no-available-copies/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 53.9%
# Likes           : 59
# Dislikes        : 15
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 373  (beats 81.00759999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764523809
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT L.book_id,
L.title,
L.author,
L.genre,
L.publication_year ,
COUNT(B.record_id) AS current_borrowers 
FROM library_books AS L
JOIN borrowing_records  AS B
ON B.book_id = L.book_id
WHERE B.return_date IS NULL
GROUP BY L.book_id, L.title, L.author, L.genre, L.publication_year, L.total_copies
HAVING COUNT(B.record_id) = L.total_copies
ORDER BY current_borrowers DESC, L.title ASC;
