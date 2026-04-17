# ================================================================
# Problem : Tree Node
# URL     : https://leetcode.com/problems/tree-node/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 75.5%
# Likes           : 1398
# Dislikes        : 132
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 347  (beats 75.08659999999998%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764076203
#
# --- Hints ---
# You can judge the node type by querying whether the node's id shows up in p_id column and whether the node's p_id is null.
# ================================================================

/* Write your T-SQL query statement below */
SELECT id ,
CASE WHEN p_id IS NULL THEN 'Root'
WHEN id IN(SELECT p_id FROM tree)
THEN  'Inner'
ELSE 'Leaf' END AS type
FROM tree
