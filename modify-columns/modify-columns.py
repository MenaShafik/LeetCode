# ================================================================
# Problem : Modify Columns
# URL     : https://leetcode.com/problems/modify-columns/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 92.3%
# Likes           : 96
# Dislikes        : 7
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 259  (beats 79.88859999999998%)
# Memory     : 65836000  (beats 98.3518%)
# Submitted  : 1774298899
#
# --- Hints ---
# Considering multiplying each salary value by 2, using a simple assignment operation. The calculation of the value is done column-wise.
# ================================================================

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.copy()
    result['salary'] = result['salary'] * 2
    return result 


