# ================================================================
# Problem : Students and Examinations
# URL     : https://leetcode.com/problems/students-and-examinations/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 61.1%
# Likes           : 3026
# Dislikes        : 363
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 536  (beats 20.598299999999945%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759846259
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT s.student_id,
s.student_name,
sub.subject_name,
COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
