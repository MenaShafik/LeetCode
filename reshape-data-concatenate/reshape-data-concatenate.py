# ================================================================
# Problem : Reshape Data: Concatenate
# URL     : https://leetcode.com/problems/reshape-data-concatenate/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 90.4%
# Likes           : 91
# Dislikes        : 7
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 272  (beats 95.37749999999996%)
# Memory     : 66804000  (beats 29.702400000000004%)
# Submitted  : 1774560094
#
# --- Hints ---
# Consider using a built-in function in pandas library with the appropriate axis argument.
# ================================================================

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    return pd.concat([df1 ,df2])
