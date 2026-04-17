# ================================================================
# Problem : Rename Columns
# URL     : https://leetcode.com/problems/rename-columns/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 85.3%
# Likes           : 83
# Dislikes        : 3
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 261  (beats 86.45460000000001%)
# Memory     : 66408000  (beats 55.595499999999994%)
# Submitted  : 1776288608
#
# --- Hints ---
# Consider using a build-in function in pandas library with a dictionary to rename the columns as specified.
# ================================================================

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={"id": "student_id",
                             "first": "first_name",
                             "last": "last_name",
                             "age": "age_in_years"
                             }, inplace=True)
    return students 
