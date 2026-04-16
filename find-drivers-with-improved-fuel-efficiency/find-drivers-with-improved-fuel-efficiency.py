# ================================================================
# Problem : Find Drivers with Improved Fuel Efficiency
# URL     : https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 46.4%
# Likes           : 42
# Dislikes        : 7
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 403  (beats 53.70320000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1765458350
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
With ct1 as
(Select t.driver_id, avg(t.distance_km/t.fuel_consumed) as first_half_avg,
avg(t1.distance_km/t1.fuel_consumed) as second_half_avg
From trips t
Join trips t1 on t.driver_id = t1.driver_id and month(t.trip_date) in (1,2,3,4,5,6) and month(t1.trip_date) in (7,8,9,10,11,12)
Group by t.driver_id)

Select ct1.driver_id, driver_name, round(first_half_avg,2) as first_half_avg, round(second_half_avg,2) as second_half_avg , round(second_half_avg - first_half_avg,2) as efficiency_improvement
From ct1
left Join drivers d on d.driver_id = ct1.driver_id
where second_half_avg - first_half_avg > 0
Order by efficiency_improvement desc,driver_name
