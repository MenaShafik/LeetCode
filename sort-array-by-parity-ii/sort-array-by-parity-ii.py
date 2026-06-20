# ==========================================================
# Problem    : Sort Array By Parity II
# URL        : https://leetcode.com/problems/sort-array-by-parity-ii/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Sorting
#
# Acceptance : 71.3%
# Likes      : 2841  |  Dislikes: 105
#
# Language   : python
# Runtime    : 1  (beats 98.0676%)
# Memory     : 14440000  (beats 34.7826%)
# Submitted  : 1781949218
# Exported   : 2026-06-20 22:35:51 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def sortArrayByParityII(self, nums):
        j = 1

        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]

        return nums

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
