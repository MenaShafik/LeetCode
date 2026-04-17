# ================================================================
# Problem : Most Common Course Pairs
# URL     : https://leetcode.com/problems/most-common-course-pairs/
# Difficulty : Hard
# Category   : Database
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 50.1%
# Likes           : 28
# Dislikes        : 1
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 238  (beats 97.4823%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766949531
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
with topStudent as (

    select user_id
    from course_completions 
    group by user_id 
   HAVING COUNT(course_id) >= 5
       AND AVG(course_rating) >= 4
)
,
CourseTransitions as (
    select cc.user_id,
    cc.course_name as first_course,
    lead(cc.course_name)over(partition by cc.user_id order by cc.completion_date) as second_course
    from course_completions as cc
    join topStudent as ts
    on cc.user_id = ts.user_id
)
select first_course,
second_course,
count(*) as transition_count 
from CourseTransitions
where second_course is not null
group by first_course,second_course
order by transition_count desc,first_course asc,second_course asc
