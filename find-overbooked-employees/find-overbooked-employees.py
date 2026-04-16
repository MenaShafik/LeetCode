# ================================================================
# Problem : Find Overbooked Employees
# URL     : https://leetcode.com/problems/find-overbooked-employees/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 44.0%
# Likes           : 46
# Dislikes        : 10
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 486  (beats 94.67190000000006%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766053647
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below

WITH weekly_meetings AS (
    SELECT
        e.employee_id,
        e.employee_name,
        e.department,
        YEARWEEK(m.meeting_date, 3) AS year_week,
        SUM(m.duration_hours) AS weekly_meeting_hours
    FROM meetings m
    JOIN employees e
        ON m.employee_id = e.employee_id
    GROUP BY
        e.employee_id,
        e.employee_name,
        e.department,
        YEARWEEK(m.meeting_date, 3)
),
meeting_heavy AS (
    SELECT
        employee_id,
        employee_name,
        department,
        COUNT(*) AS meeting_heavy_weeks
    FROM weekly_meetings
    WHERE weekly_meeting_hours > 20   -- > 50% of 40 hours
    GROUP BY
        employee_id,
        employee_name,
        department
)
SELECT
    employee_id,
    employee_name,
    department,
    meeting_heavy_weeks
FROM meeting_heavy
WHERE meeting_heavy_weeks >= 2
ORDER BY
    meeting_heavy_weeks DESC,
    employee_name ASC;

