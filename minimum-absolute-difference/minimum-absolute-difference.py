# ================================================================
# Problem : Minimum Absolute Difference
# URL     : https://leetcode.com/problems/minimum-absolute-difference/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 75.1%
# Likes           : 2890
# Dislikes        : 95
#
# --- My Submission ---
# Language   : python
# Runtime    : 67  (beats 83.20729999999999%)
# Memory     : 21508000  (beats 83.81240000000001%)
# Submitted  : 1769454041
#
# --- Hints ---
# Find the minimum absolute difference between two elements in the array.
# The minimum absolute difference must be a difference between two consecutive elements in the sorted array.
# ================================================================

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        res = []
        min_diff = float('inf')
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                res.append([arr[i - 1], arr[i]])
        
        return res
