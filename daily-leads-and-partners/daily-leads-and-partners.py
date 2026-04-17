# ================================================================
# Problem : Daily Leads and Partners
# URL     : https://leetcode.com/problems/daily-leads-and-partners/
# Difficulty : Easy
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 86.6%
# Likes           : 635
# Dislikes        : 36
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 431  (beats 73.22439999999995%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1764112747
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
SELECT date_id,
make_name,
count(distinct lead_id ) as unique_leads ,
count(distinct partner_id) as unique_partners 
from dailysales
group by date_id,
make_name
