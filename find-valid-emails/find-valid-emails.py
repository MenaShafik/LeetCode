# ================================================================
# Problem : Find Valid Emails
# URL     : https://leetcode.com/problems/find-valid-emails/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 44.0%
# Likes           : 63
# Dislikes        : 9
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 273  (beats 84.7456%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764508388
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT user_id,
email
FROM Users
WHERE
email LIKE '[A-Za-z0-9_]%@[^0-9]%[^0-9].com'
AND email NOT LIKE '%[^A-Za-z0-9_@.]%'
AND email not like '%.%@%.com'
order  by user_id
