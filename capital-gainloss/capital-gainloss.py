# ================================================================
# Problem : Capital Gain/Loss
# URL     : https://leetcode.com/problems/capital-gainloss/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 84.6%
# Likes           : 930
# Dislikes        : 51
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 711  (beats 92.57220000000004%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764164240
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT 
stock_name,
SUM(CASE WHEN operation = 'BUY' THEN -price
ELSE price
END)AS capital_gain_loss
FROM Stocks 
GROUP BY stock_name

