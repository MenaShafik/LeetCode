# ================================================================
# Problem : Market Analysis I
# URL     : https://leetcode.com/problems/market-analysis-i/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 57.3%
# Likes           : 755
# Dislikes        : 74
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1158  (beats 97.79439999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764417231
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
    SELECT u.user_id AS buyer_id,
    U.join_date,
    isnull(COUNT(O.buyer_id),0) AS orders_in_2019
    FROM Users AS U
    LEFT JOIN Orders AS O
    ON U.user_id = O.buyer_id AND YEAR(O.order_date) = 2019
    GROUP BY u.user_id,U.join_date
