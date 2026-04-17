# ================================================================
# Problem : Get the Size of a DataFrame
# URL     : https://leetcode.com/problems/get-the-size-of-a-dataframe/
# Difficulty : Easy
# Category   : pandas
# Tags       : 
#
# --- Community Stats ---
# Acceptance Rate : 84.8%
# Likes           : 155
# Dislikes        : 14
#
# --- My Submission ---
# Language   : pythondata
# Runtime    : 263  (beats 79.6836%)
# Memory     : 66312000  (beats 59.62110000000002%)
# Submitted  : 1776197797
#
# --- Hints ---
# Consider using a built-in function in pandas library to get the size of a DataFrame.
# ================================================================

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
