# ================================================================
# Problem : Classes With at Least 5 Students
# URL     : https://leetcode.com/problems/classes-with-at-least-5-students/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 63.6%
# Likes           : 1335
# Dislikes        : 1084
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 519  (beats 99.22480000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760537261
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select class
from Courses
group by class
having count(class) >= 5 and count(student) > 1
