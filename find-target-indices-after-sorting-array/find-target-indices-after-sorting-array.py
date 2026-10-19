# ==========================================================
# Problem    : Find Target Indices After Sorting Array
# URL        : https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Binary Search, Sorting
#
# Acceptance : 81.5%
# Likes      : 2188  |  Dislikes: 109
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12168000  (beats 98.5781%)
# Submitted  : 1792416616
# Exported   : 2026-10-19 16:47:17 UTC
#
# Hints: Try "sorting" the array first.
#   Now find all indices in the array whose values are equal to target.
# ==========================================================
class Solution(object):
    def targetIndices(self, nums, target):
        stack = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                stack.append(i)

        return stack
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
