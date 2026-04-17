# ================================================================
# Problem : Create a New Column
# URL     : https://leetcode.com/problems/create-a-new-column/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 90.1%
# Likes           : 109
# Dislikes        : 6
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 257  (beats 88.2315%)
# Memory     : 65780000  (beats 99.1674%)
# Submitted  : 1774382502
#
# --- Hints ---
# Consider using the `[]` brackets with the new column name at the left side of the assignment. The calculation of the value is done element-wise.
# ================================================================

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']= employees['salary']*2
    return employees
