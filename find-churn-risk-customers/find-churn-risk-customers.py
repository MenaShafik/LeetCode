# ================================================================
# Problem : Find Churn Risk Customers
# URL     : https://leetcode.com/problems/find-churn-risk-customers/
# Difficulty : Medium
# Category   : Database
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 46.7%
# Likes           : 32
# Dislikes        : 1
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 291  (beats 99.28859999999999%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766237245
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
WITH LAST AS (
    SELECT 
        user_id,
        plan_name AS current_plan,
        monthly_amount AS current_monthly_amount,
        event_type AS last_event_type,
        ROW_NUMBER() OVER (
            PARTITION BY user_id 
            ORDER BY event_date DESC
        ) AS RN
    FROM subscription_events
),
DA_TE AS (
    SELECT 
        user_id,
        MIN(event_date) AS first_event_date,
        MAX(event_date) AS last_event_date,
        MAX(monthly_amount) AS max_historical_amount,
        SUM(CASE WHEN event_type = 'downgrade' THEN 1 ELSE 0 END) AS downgrade_count
    FROM subscription_events
    GROUP BY user_id
)
SELECT 
    D.user_id,
    L.current_plan,
    L.current_monthly_amount,
    D.max_historical_amount,
    DATEDIFF(D.last_event_date, D.first_event_date) AS days_as_subscriber
FROM DA_TE AS D
JOIN LAST AS L
    ON D.user_id = L.user_id 
   AND L.RN = 1
WHERE L.last_event_type <> 'cancel'
  AND D.downgrade_count > 0
  AND L.current_monthly_amount < 0.5 * D.max_historical_amount
  AND DATEDIFF(D.last_event_date, D.first_event_date) >= 60
ORDER BY days_as_subscriber DESC, D.user_id;

