# ================================================================
# Problem : Change Data Type
# URL     : https://leetcode.com/problems/change-data-type/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 87.3%
# Likes           : 89
# Dislikes        : 9
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 266  (beats 79.94039999999994%)
# Memory     : 66088000  (beats 97.5907%)
# Submitted  : 1774383429
#
# --- Hints ---
# Consider using a build-in function in pandas library with a dictionary to convert the datatype of columns as specified.
# ================================================================

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
