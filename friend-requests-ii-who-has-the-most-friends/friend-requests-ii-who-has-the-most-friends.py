# ================================================================
# Problem : Friend Requests II: Who Has the Most Friends
# URL     : https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 62.5%
# Likes           : 984
# Dislikes        : 152
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 331  (beats 25.202500000000043%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761758165
#
# --- Hints ---
# Being friends is bidirectional. If you accept someone's adding friend request, both you and the other person will have one more friend.
# ================================================================

/* Write your T-SQL query statement below */
with test as (

    select accepter_id as id,
    count(accepter_id) cnt
    from RequestAccepted
    group by accepter_id
    union all
    select requester_id as id,
    count(requester_id) as cnt
    from RequestAccepted
    group by requester_id
)
select top 1 id,sum(cnt) as num from test
group by id
order by sum(cnt) desc
