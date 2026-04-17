# ================================================================
# Problem : Find Users With Valid E-Mails
# URL     : https://leetcode.com/problems/find-users-with-valid-e-mails/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 36.2%
# Likes           : 709
# Dislikes        : 314
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 703  (beats 73.79739999999995%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761778284
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
/* Write your T-SQL query statement below */
SELECT 
user_id,
name,
mail   
FROM Users              
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
and mail like '%@leetcode.com' COLLATE utf8mb4_bin;
