# ================================================================
# Problem : Display the First Three Rows
# URL     : https://leetcode.com/problems/display-the-first-three-rows/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 93.0%
# Likes           : 123
# Dislikes        : 26
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 244  (beats 98.18710000000002%)
# Memory     : 66480000  (beats 39.94690000000001%)
# Submitted  : 1774216503
#
# --- Hints ---
# Consider using a built-in function in pandas library to retrieve the initial rows.
# ================================================================

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    three= employees.head(3)
    return three
