# ================================================================
# Problem : Customers Who Never Order
# URL     : https://leetcode.com/problems/customers-who-never-order/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 71.7%
# Likes           : 3088
# Dislikes        : 160
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 386  (beats 41.1533%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761339234
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT C.name  AS Customers 
FROM Customers AS C
LEFT JOIN Orders AS O
ON C.id = O.customerId  
WHERE  O.customerId IS NULL

