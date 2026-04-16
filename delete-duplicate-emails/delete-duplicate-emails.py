# ================================================================
# Problem : Delete Duplicate Emails
# URL     : https://leetcode.com/problems/delete-duplicate-emails/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 65.9%
# Likes           : 2099
# Dislikes        : 429
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 502  (beats 28.321199999999948%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761568404
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */

 delete p from person as p,person as q
 where p.id > q.id and p.email  = q.email

