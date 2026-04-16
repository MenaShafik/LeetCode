# ================================================================
# Problem : Customer Who Visited but Did Not Make Any Transactions
# URL     : https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 67.7%
# Likes           : 3500
# Dislikes        : 458
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1296  (beats 41.616000000000525%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1759829747
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT distinct customer_id,
count(customer_id) as count_no_trans 
FROM visits AS V
LEFT JOIN Transactions AS T
ON V.visit_id  = T.visit_id
where T.visit_id is null
group by customer_id;
