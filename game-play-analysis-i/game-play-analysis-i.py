# ================================================================
# Problem : Game Play Analysis I
# URL     : https://leetcode.com/problems/game-play-analysis-i/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 76.3%
# Likes           : 1100
# Dislikes        : 47
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1172  (beats 76.2626000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1763420204
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select t.player_id,first_login
from (
select player_id,
event_date as first_login ,
rank() over(partition by player_id order by event_date) as rnk
from activity
)t
where rnk = 1
