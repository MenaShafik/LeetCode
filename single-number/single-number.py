# ================================================================
# Problem : Single Number
# URL     : https://leetcode.com/problems/single-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Bit Manipulation
#
# --- Community Stats ---
# Acceptance Rate : 77.6%
# Likes           : 18854
# Dislikes        : 905
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13964000  (beats 58.300399999999996%)
# Submitted  : 1773870681
#
# --- Hints ---
# Think about the XOR (^) operator's property.
# ================================================================

class Solution(object):
    def singleNumber(self, nums):
        ret = 0
        for i in nums:
            ret ^= i
        return ret
        """
        :type nums: List[int]
        :rtype: int
        """
        
