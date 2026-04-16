# ================================================================
# Problem : Biggest Single Number
# URL     : https://leetcode.com/problems/biggest-single-number/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 71.2%
# Likes           : 975
# Dislikes        : 203
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 324  (beats 62.75129999999998%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760539434
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */

select max(num) as num 
from (
    select num
     from MyNumbers
     group by num 
     having count(*) =1
) as a
