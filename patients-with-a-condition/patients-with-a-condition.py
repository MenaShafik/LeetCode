# ================================================================
# Problem : Patients With a Condition
# URL     : https://leetcode.com/problems/patients-with-a-condition/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 38.9%
# Likes           : 878
# Dislikes        : 657
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 283  (beats 95.65789999999997%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1761776277
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT patient_id ,
patient_name ,
conditions    
FROM Patients 
WHERE conditions
LIKE '% DIAB1%' 
or conditions
 like 'DIAB1%';
