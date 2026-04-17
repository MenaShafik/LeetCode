# ================================================================
# Problem : Find Consistently Improving Employees
# URL     : https://leetcode.com/problems/find-consistently-improving-employees/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 55.9%
# Likes           : 48
# Dislikes        : 2
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 367  (beats 55.13950000000004%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766320340
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
WITH RANKED AS (
SELECT 
employee_id ,
rating ,
review_date ,
ROW_NUMBER() OVER(PARTITION BY employee_id ORDER BY review_date DESC) AS RN
FROM performance_reviews 
),
LAST_THREE AS (
    SELECT  
    employee_id,
        rating,
        review_date,
        LAG(RATING) OVER(PARTITION BY employee_id ORDER BY review_date ) AS PREV
    FROM RANKED
    WHERE RN <=3
),
VALID AS (
    SELECT 
    employee_id ,
MIN(rating) AS F_RATE,
MAX(rating) AS L_RATE
FROM LAST_THREE
GROUP BY employee_id
HAVING COUNT(*) = 3
AND MIN(rating) < MAX(rating)
AND SUM( CASE WHEN PREV IS NOT NULL 
                     AND rating <= PREV 
                THEN 1 ELSE 0 
            END
        ) = 0
)
SELECT
    v.employee_id,
    e.name,
    v.L_RATE - v.F_RATE AS improvement_score
FROM VALID v
JOIN employees e
    ON v.employee_id = e.employee_id
ORDER BY improvement_score DESC, e.name ASC;
