# ================================================================
# Problem : Actors and Directors Who Cooperated At Least Three Times
# URL     : https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 71.0%
# Likes           : 792
# Dislikes        : 57
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 604  (beats 99.508%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764018788
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
/*SELECT actor_id,
director_id 
FROM ActorDirector 
WHERE director_id = actor_id    
GROUP BY actor_id,director_id 
HAVING COUNT(*) >= 3
*/
SELECT actor_id,
T.director_id
FROM (
    SELECT actor_id,
    director_id,
    COUNT(*) AS C
    FROM ActorDirector 
    GROUP BY actor_id,director_id 
)T
WHERE C >=3
