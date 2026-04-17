# ================================================================
# Problem : Investments in 2016
# URL     : https://leetcode.com/problems/investments-in-2016/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 51.0%
# Likes           : 942
# Dislikes        : 635
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 564  (beats 56.777799999999964%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761779126
#
# --- Hints ---
# Make the (LAT, LON) a pair to represent the location information
# ================================================================

/* Write your T-SQL query statement below */
select round(sum(TIV_2016),2) as tiv_2016
from insurance
where TIV_2015 in
(select TIV_2015 from insurance
group by TIV_2015
having count(TIV_2015) >1)
and concat(LAT, LON) not in
(select concat(LAT, LON) from insurance
group by LAT, LON
having count(concat(LAT, LON)) >1);
