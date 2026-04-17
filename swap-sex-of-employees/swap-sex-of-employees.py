# ================================================================
# Problem : Swap Sex of Employees
# URL     : https://leetcode.com/problems/swap-sex-of-employees/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 84.6%
# Likes           : 1870
# Dislikes        : 573
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 259  (beats 93.86500000000002%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1763818153
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
update salary
set
sex = CASE WHEN sex = 'm' THEN 'f'
else 'm'
END

