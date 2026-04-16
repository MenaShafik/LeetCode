# ================================================================
# Problem : DNA Pattern Recognition 
# URL     : https://leetcode.com/problems/dna-pattern-recognition/
# Difficulty : Medium
# Category   : Database
# Tags       : Database
#
# --- Community Stats ---
# Acceptance Rate : 84.9%
# Likes           : 60
# Dislikes        : 7
#
# --- My Submission ---
# Language   : mssql
# Runtime    : 269  (beats 82.75890000000001%)
# Memory     : 0  (beats 100.0%)
# Submitted  : 1765372559
#
# --- Hints ---
# N/A
# ================================================================

/* Write your T-SQL query statement below */
with norm as (
    select 
    sample_id,
    dna_sequence,
   species,
   case when dna_sequence like 'ATG%' then 1 else 0 end as has_start,

   case when dna_sequence like '%TAA' or
     dna_sequence like '%TAG' or 
     dna_sequence like '%TGA' 
    then 1 else 0 end as has_stop,

    case when dna_sequence like '%ATAT'
OR dna_sequence like 'ATAT%'
OR dna_sequence like '%ATAT%'
    then 1 else 0 end as has_atat,

    case when dna_sequence like '%GGG%' or
     dna_sequence like '%GGG' or 
     dna_sequence like 'GGG%' OR
     dna_sequence like '%GGG%' OR
     dna_sequence like '%GGGG%' OR
     dna_sequence like '%GGGG' OR
     dna_sequence like 'GGGG%' 
    then 1 else 0 end as has_ggg    
   from Samples 
)
select * from norm
