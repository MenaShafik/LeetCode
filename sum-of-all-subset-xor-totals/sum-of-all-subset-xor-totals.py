# ==========================================================
# Problem    : Sum of All Subset XOR Totals
# URL        : https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration
#
# Acceptance : 90.1%
# Likes      : 2743  |  Dislikes: 361
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12444000  (beats 29.032200000000003%)
# Submitted  : 1791035886
# Exported   : 2026-10-03 15:55:21 UTC
#
# Hints: Is there a way to iterate through all the subsets of the array?
#   Can we use recursion to efficiently iterate through all the subsets?
# ==========================================================
from itertools import combinations
class Solution(object):
    def subsetXORSum(self, nums):
        xor = 0
        for i in nums:
            xor |= i
        return xor * (2 ** (len(nums) - 1))
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
