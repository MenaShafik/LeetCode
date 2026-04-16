# ================================================================
# Problem : Duplicate Emails
# URL     : https://leetcode.com/problems/duplicate-emails/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 73.6%
# Likes           : 2461
# Dislikes        : 89
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 349  (beats 99.44400000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759699755
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select  email as Email
from Person
group by email
having count(*) > 1
