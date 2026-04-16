# ================================================================
# Problem : Queries Quality and Percentage
# URL     : https://leetcode.com/problems/queries-quality-and-percentage/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 52.8%
# Likes           : 1125
# Dislikes        : 546
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1675  (beats 5.628099999999912%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760356631
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT query_name ,
ROUND(SUM(rating * 1.0 /position ) / COUNT(query_name ),2) AS quality ,
ROUND((SUM(CASE WHEN rating <3 THEN 1
ELSE 0 END) * 100.0) / COUNT(query_name),2) AS poor_query_percentage
FROM Queries 
WHERE query_name IS NOT NULL
GROUP BY query_name 
ORDER BY query_name DESC 
