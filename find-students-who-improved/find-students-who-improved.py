# ================================================================
# Problem : Find Students Who Improved
# URL     : https://leetcode.com/problems/find-students-who-improved/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 48.3%
# Likes           : 102
# Dislikes        : 10
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 262  (beats 98.0856%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764337964
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
/* Write your T-SQL query statement below */
SELECT student_id,
subject  ,
MIN_SCORE AS first_score ,
MAX_SCORE AS latest_score
from
(SELECT student_id,
subject,
score,
exam_date,
FIRST_VALUE(score) OVER(PARTITION BY student_id,subject order by exam_date ASC) AS MIN_SCORE,
LAST_VALUE(score) OVER(PARTITION BY student_id,subject order by exam_date ASC) AS MAX_SCORE ,
ROW_NUMBER()OVER(PARTITION BY student_id,subject order by exam_date DESC) AS RN
from scores )Y
WHERE RN = 1 AND MIN_SCORE < MAX_SCORE

