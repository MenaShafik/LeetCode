# ================================================================
# Problem : Game Play Analysis IV
# URL     : https://leetcode.com/problems/game-play-analysis-iv/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 41.1%
# Likes           : 1509
# Dislikes        : 250
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1375  (beats 41.39660000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761778997
#
# --- Hints ---
# N/A
# ================================================================

select round((count(distinct b.player_id)+0.0)/(count(distinct a.player_id)+0.0),2)
as fraction from Activity a
left join Activity b
on a.player_id = b.player_id and datediff(day, a.event_date, b.event_date)=1
where a.event_date in
(select min(c.event_date) from Activity c group by c.player_id having c.player_id = a.player_id)
