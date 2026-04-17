# ================================================================
# Problem : Find Product Recommendation Pairs
# URL     : https://leetcode.com/problems/find-product-recommendation-pairs/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 61.5%
# Likes           : 86
# Dislikes        : 5
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 548  (beats 87.43539999999996%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1766404023
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
SELECT A.product_id AS product1_id,
B.product_id AS product2_id,
C.category AS product1_category,
D.category AS product2_category,
COUNT(A.user_id) AS customer_count
FROM ProductPurchases AS A
JOIN ProductPurchases AS B
ON A.user_id = B.user_id
JOIN ProductInfo  AS C
ON A.product_id = C.product_id
JOIN ProductInfo  AS D
ON B.product_id = D.product_id
WHERE B.product_id > A.product_id
GROUP BY A.product_id,B.product_id
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC, product1_id,product2_id
