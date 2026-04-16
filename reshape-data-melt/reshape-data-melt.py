# ================================================================
# Problem : Reshape Data: Melt
# URL     : https://leetcode.com/problems/reshape-data-melt/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 85.9%
# Likes           : 113
# Dislikes        : 4
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 259  (beats 100.0%)
# Memory     : 66328000  (beats 92.1344%)
# Submitted  : 1775512449
#
# --- Hints ---
# Consider using a built-in function in pandas library to transform the data
# ================================================================

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars="product",var_name="quarter",value_name="sales")
