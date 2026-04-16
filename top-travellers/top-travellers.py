# ================================================================
# Problem : Top Travellers
# URL     : https://leetcode.com/problems/top-travellers/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 57.2%
# Likes           : 747
# Dislikes        : 85
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 614  (beats 68.27700000000009%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1763736460
#
# --- Hints ---
# N/A
# ================================================================

SELECT DISTINCT name,
COALESCE(sum(distance) over(partition by user_id),0) as travelled_distance
From Users AS U
Left Join Rides AS R
on U.id=R.User_id
Order by travelled_distance DESC, Name ASC
