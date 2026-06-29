# ==========================================================
# Problem    : Monotonic Array
# URL        : https://leetcode.com/problems/monotonic-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 62.4%
# Likes      : 3295  |  Dislikes: 107
#
# Language   : python
# Runtime    : 69  (beats 60.095599999999926%)
# Memory     : 20540000  (beats 31.34080000000001%)
# Submitted  : 1782745879
# Exported   : 2026-06-29 15:13:50 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isMonotonic(self, nums):
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                inc = False
            if nums[i] > nums[i - 1]:
                dec = False
        return inc or dec
        """
        :type nums: List[int]
        :rtype: bool
        """
        
