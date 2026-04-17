# ================================================================
# Problem : Triangle Judgement
# URL     : https://leetcode.com/problems/triangle-judgement/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 74.7%
# Likes           : 864
# Dislikes        : 239
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 285  (beats 54.43390000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760612564
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select x,y,z,
case when x+y > z and x+z > y and y+z > x then 'Yes'
else 'No' 
end as triangle 
from Triangle 

