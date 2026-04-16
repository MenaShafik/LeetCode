# ================================================================
# Problem : Find COVID Recovery Patients
# URL     : https://leetcode.com/problems/find-covid-recovery-patients/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 41.7%
# Likes           : 54
# Dislikes        : 8
#
# --- My Submission ---
# Language   : mysql
# Runtime    : 453  (beats 99.2307%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764962897
#
# --- Hints ---
# N/A
# ================================================================

# Write your MySQL query statement below
WITH first_positive AS (
SELECT
patient_id,
MIN(test_date) AS first_pos_date
FROM covid_tests
WHERE result = 'Positive'
GROUP BY patient_id
),
first_negative_after AS (
SELECT
c.patient_id,
MIN(c.test_date) AS first_neg_date
FROM covid_tests c
JOIN first_positive fp
ON fp.patient_id = c.patient_id
AND c.result = 'Negative'
AND c.test_date > fp.first_pos_date
GROUP BY c.patient_id
)
SELECT
p.patient_id,
p.patient_name,
p.age,
DATEDIFF(fn.first_neg_date, fp.first_pos_date) AS recovery_time
FROM patients p
JOIN first_positive fp ON p.patient_id = fp.patient_id
JOIN first_negative_after fn ON p.patient_id = fn.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;
