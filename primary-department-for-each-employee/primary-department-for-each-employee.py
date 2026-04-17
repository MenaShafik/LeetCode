# ================================================================
# Problem : Primary Department for Each Employee
# URL     : https://leetcode.com/problems/primary-department-for-each-employee/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 74.2%
# Likes           : 865
# Dislikes        : 271
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 394  (beats 96.04940000000003%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760612019
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select employee_id ,department_id 
from Employee 
where primary_flag = 'Y' or employee_id in (

    select employee_id 
    from employee
    group by employee_id
    having count(employee_id) = 1
)
