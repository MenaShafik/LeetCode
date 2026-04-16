# ================================================================
# Problem : Concatenation of Array
# URL     : https://leetcode.com/problems/concatenation-of-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# --- Community Stats ---
# Acceptance Rate : 90.4%
# Likes           : 4194
# Dislikes        : 462
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12372000  (beats 99.8894%)
# Submitted  : 1775159901
#
# --- Hints ---
# Build an array of size 2 * n and assign nums[i] to ans[i] and ans[i + n]
# ================================================================

class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
