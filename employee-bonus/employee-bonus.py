# ================================================================
# Problem : Employee Bonus
# URL     : https://leetcode.com/problems/employee-bonus/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 77.3%
# Likes           : 1603
# Dislikes        : 302
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 636  (beats 58.65109999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759844130
#
# --- Hints ---
# If the EmpId in table Employee has no match in table Bonus, we consider that the corresponding bonus is null and null is smaller than 1000.
# Inner join is the default join, we can solve the mismatching problem by using outer join.
# ================================================================

/* Write your T-SQL query statement below */
SELECT E.name,
B.bonus
FROM  Employee AS E
LEFT JOIN Bonus AS B
ON E.empId  = B.empId 
where B.bonus < 1000 or B.bonus is null
