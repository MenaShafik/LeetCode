# ================================================================
# Problem : Drop Duplicate Rows
# URL     : https://leetcode.com/problems/drop-duplicate-rows/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 85.2%
# Likes           : 134
# Dislikes        : 6
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 256  (beats 91.30340000000007%)
# Memory     : 66684000  (beats 93.2443%)
# Submitted  : 1776288807
#
# --- Hints ---
# Consider using a build-in function in pandas library to remove the duplicate rows based on specified data.
# ================================================================

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=["email"], inplace=True)
    return customers
