# ================================================================
# Problem : Reformat Department Table
# URL     : https://leetcode.com/problems/reformat-department-table/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 76.3%
# Likes           : 858
# Dislikes        : 645
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 770  (beats 93.77819999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764242309
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT id,
sum(case when month = 'Jan' then revenue end) as Jan_Revenue,
sum(case when month = 'Feb' then revenue end) as Feb_Revenue,
sum(case when month = 'Mar' then revenue end) as Mar_Revenue,
sum(case when month = 'Apr' then revenue end) as Apr_Revenue,
sum(case when month = 'May' then revenue end) as May_Revenue,
sum(case when month = 'Jun' then revenue end) as Jun_Revenue,
sum(case when month = 'Jul' then revenue end) as Jul_Revenue,
sum(case when month = 'Aug' then revenue end) as Aug_Revenue,
sum(case when month = 'Sep' then revenue end) as Sep_Revenue,
sum(case when month = 'Oct' then revenue end) as Oct_Revenue,
sum(case when month = 'Nov' then revenue end) as Nov_Revenue,
sum(case when month = 'Dec' then revenue end) as Dec_Revenue
FROM Department 
GROUP BY id
