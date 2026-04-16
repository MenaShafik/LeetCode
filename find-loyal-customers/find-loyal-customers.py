# ================================================================
# Problem : Find Loyal Customers
# URL     : https://leetcode.com/problems/find-loyal-customers/
# Difficulty : Medium
# Category   : Database
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 60.4%
# Likes           : 44
# Dislikes        : 1
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 304  (beats 74.3894%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1765294212
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
WITH cte AS (
    SELECT 
        customer_id, 
        COUNT(CASE WHEN transaction_type = 'purchase' THEN 1 END) AS trans,
        ROUND(
            COUNT(CASE WHEN transaction_type = 'refund' THEN 1 END) * 100.0 / COUNT(*), 
            2
        ) AS refund_rate
    FROM customer_transactions
    GROUP BY customer_id
    HAVING 
        DATEDIFF(MAX(transaction_date), MIN(transaction_date)) > 29 
        AND refund_rate < 20 
        AND trans >= 3
)
SELECT customer_id
FROM cte
ORDER BY customer_id ASC;

