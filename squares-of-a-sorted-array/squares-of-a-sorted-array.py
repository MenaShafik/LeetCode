# ==========================================================
# Problem    : Squares of a Sorted Array
# URL        : https://leetcode.com/problems/squares-of-a-sorted-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Sorting
#
# Acceptance : 73.9%
# Likes      : 10339  |  Dislikes: 281
#
# Language   : python
# Runtime    : 2  (beats 97.6288%)
# Memory     : 14168000  (beats 72.75019999999999%)
# Submitted  : 1782394488
# Exported   : 2026-06-25 13:38:13 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def sortedSquares(self, nums):
        stack = []
        for num in nums:
            stack.append(num**2)
        stack.sort()
        return stack
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
