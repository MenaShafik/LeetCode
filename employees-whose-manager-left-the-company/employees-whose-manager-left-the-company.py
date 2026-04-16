# ================================================================
# Problem : Employees Whose Manager Left the Company
# URL     : https://leetcode.com/problems/employees-whose-manager-left-the-company/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 48.7%
# Likes           : 629
# Dislikes        : 55
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 346  (beats 97.51600000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760820547
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select employee_id 
from Employees
 where salary < 30000
 and manager_id is not null
and  manager_id not in(select employee_id from Employees ) 
order by employee_id
