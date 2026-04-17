# ================================================================
# Problem : Managers with at Least 5 Direct Reports
# URL     : https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 49.0%
# Likes           : 1770
# Dislikes        : 191
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 752  (beats 17.68389999999999%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760035583
#
# --- Hints ---
# Try to get all the mangerIDs that have count bigger than 5
# Use the last hint's result as a table and do join with origin table at id equals to managerId
# This is a very good example to show the performance of SQL code. Try to work out other solutions and you may be surprised by running time difference.
# If your solution uses 'IN' function and runs more than 5 seconds, try to optimize it by using 'JOIN' instead.
# ================================================================

/* Write your T-SQL query statement below */
select E.name 
from Employee as E
 join(
select managerId 
from Employee 
where managerId is not null
group by managerId 
having count(*) >= 5
 ) as EM
on E.id = EM.managerId 


