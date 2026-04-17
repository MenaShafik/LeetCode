# ================================================================
# Problem : Customer Placing the Largest Number of Orders
# URL     : https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 64.4%
# Likes           : 1227
# Dislikes        : 100
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 438  (beats 84.89019999999996%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764684761
#
# --- Hints ---
# MySQL uses a different expression to get the first records other than MSSQL's TOP expression.
# ================================================================

/* Write your T-SQL query statement below */
 WITH ABC AS
 (
    SELECT 
    customer_number ,
   COUNT(customer_number) AS CNT
FROM Orders 
GROUP BY customer_number 
 )
 SELECT customer_number FROM ABC WHERE CNT = (SELECT MAX(CNT) FROM ABC)
