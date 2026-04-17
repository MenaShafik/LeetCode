# ================================================================
# Problem : Replace Employee ID With The Unique Identifier
# URL     : https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 83.5%
# Likes           : 2061
# Dislikes        : 162
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 967  (beats 91.19710000000005%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759827178
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
EU.unique_id,
E.name
FROM Employees AS E
LEFT JOIN EmployeeUNI AS EU
ON E.id = EU.id;
