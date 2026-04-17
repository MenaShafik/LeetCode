# ================================================================
# Problem : Combine Two Tables
# URL     : https://leetcode.com/problems/combine-two-tables/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 79.4%
# Likes           : 4375
# Dislikes        : 258
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 413  (beats 68.57639999999996%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760706474
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT P.firstName,
 P.lastName,
 A.city,
A.state
FROM Person AS P
LEFT JOIN Address AS A
ON P.personId = A.personId 

