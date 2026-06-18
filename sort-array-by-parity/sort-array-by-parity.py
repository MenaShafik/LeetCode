# ==========================================================
# Problem    : Sort Array By Parity
# URL        : https://leetcode.com/problems/sort-array-by-parity/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Sorting
#
# Acceptance : 76.6%
# Likes      : 5724  |  Dislikes: 157
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13088000  (beats 36.48639999999998%)
# Submitted  : 1781778550
# Exported   : 2026-06-18 10:31:01 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
