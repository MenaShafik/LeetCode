# ================================================================
# Problem : Sales Person
# URL     : https://leetcode.com/problems/sales-person/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 65.9%
# Likes           : 1429
# Dislikes        : 123
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 608  (beats 47.15290000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1763674817
#
# --- Hints ---
# You need to query who sold to company 'RED' first, then output the sales person who is not in the first query result.
# ================================================================

/* Write your T-SQL query statement below */
select name from salesperson where name not in (
select s.name from
orders o join salesperson s on s.sales_id=o.sales_id
join company c on c.com_id=o.com_id
where c.name='RED'
)

