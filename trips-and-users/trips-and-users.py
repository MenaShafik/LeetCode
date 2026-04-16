# ================================================================
# Problem : Trips and Users
# URL     : https://leetcode.com/problems/trips-and-users/
# Difficulty : Hard
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 38.1%
# Likes           : 1436
# Dislikes        : 711
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 478  (beats 97.97220000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766762617
#
# --- Hints ---
# N/A
# ================================================================

select Request_at as Day,
round(sum(case when Status != 'completed' then 1 else 0 end)/count(*),2) as 'Cancellation Rate' from
Trips
where Client_Id not in (select Users_Id from Users where Banned = 'Yes')
and Driver_Id not in (select Users_id from Users where Banned = 'Yes')
and Request_at BETWEEN '2013-10-01' AND '2013-10-03'
group by Request_at
