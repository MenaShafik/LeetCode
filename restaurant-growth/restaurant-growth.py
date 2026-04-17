# ================================================================
# Problem : Restaurant Growth
# URL     : https://leetcode.com/problems/restaurant-growth/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 58.6%
# Likes           : 1171
# Dislikes        : 388
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 537  (beats 7.997299999999988%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761661763
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select visited_on,
(select sum(amount) from Customer
where visited_on between dateadd(day,-6,c.visited_on) and c.visited_on) as amount,
(select round(cast(sum(amount) as decimal(10,2))/7,2) from Customer
where visited_on between dateadd(day,-6,c.visited_on) and c.visited_on) as average_amount
from Customer c
where visited_on >= (
select dateadd(day,6,min(visited_on))
from Customer
)
group by visited_on
order by visited_on
