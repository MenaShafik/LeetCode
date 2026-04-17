# ================================================================
# Problem : Number of Unique Subjects Taught by Each Teacher
# URL     : https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 89.2%
# Likes           : 750
# Dislikes        : 57
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1253  (beats 96.87000000000005%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759829904
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT teacher_id,
count( distinct subject_id) as cnt 
FROM teacher
GROUP BY teacher_id;
