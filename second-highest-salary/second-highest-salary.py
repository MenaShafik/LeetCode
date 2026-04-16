# ================================================================
# Problem : Second Highest Salary
# URL     : https://leetcode.com/problems/second-highest-salary/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 46.8%
# Likes           : 4265
# Dislikes        : 1014
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 332  (beats 94.76200000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761568422
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select MAX(salary) as SecondHighestSalary from
(
SELECT *,
DENSE_RANK()over(order by salary desc) as row_id
from Employee
)T
where row_id = 2 
