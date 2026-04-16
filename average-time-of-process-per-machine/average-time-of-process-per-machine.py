# ================================================================
# Problem : Average Time of Process per Machine
# URL     : https://leetcode.com/problems/average-time-of-process-per-machine/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 66.8%
# Likes           : 2459
# Dislikes        : 245
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 236  (beats 98.8054%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1760215675
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
select a1.machine_id,
round(avg(a2.timestamp - a1.timestamp),3) as processing_time 
from activity as a1
join activity as a2
on a1.machine_id = a2.machine_id AND
a1.process_id = a2.process_id AND
a1.activity_type = 'start' AND
a2.activity_type = 'end' 
group by a1.machine_id
