# ================================================================
# Problem : Employees Earning More Than Their Managers
# URL     : https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 73.1%
# Likes           : 3170
# Dislikes        : 302
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 420  (beats 84.26990000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760966475
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT E.name as Employee 
FROM Employee AS E
JOIN Employee AS M
ON E.managerId = M.id 
WHERE E.salary > M.salary 

