# ==========================================================
# Problem    : Missing Number
# URL        : https://leetcode.com/problems/missing-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
#
# Acceptance : 71.9%
# Likes      : 14332  |  Dislikes: 3477
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13800000  (beats 10.136000000000001%)
# Submitted  : 1777671491
# Exported   : 2026-05-01 21:39:04 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def missingNumber(self, nums):
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

        """
        :type nums: List[int]
        :rtype: int
        """
        
