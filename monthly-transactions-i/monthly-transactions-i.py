# ================================================================
# Problem : Monthly Transactions I
# URL     : https://leetcode.com/problems/monthly-transactions-i/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 59.1%
# Likes           : 1436
# Dislikes        : 133
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 1625  (beats 36.21510000000049%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761054218
#
# --- Hints ---
# N/A
# ================================================================

SELECT
FORMAT(trans_date, 'yyyy-MM') AS month,
country,
COUNT(*) AS trans_count,
SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY FORMAT(trans_date, 'yyyy-MM'), country;
