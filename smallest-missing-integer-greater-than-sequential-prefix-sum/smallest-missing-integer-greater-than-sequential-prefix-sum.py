# ==========================================================
# Problem    : Smallest Missing Integer Greater Than Sequential Prefix Sum
# URL        : https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 50.0%
# Likes      : 444  |  Dislikes: 452
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12384000  (beats 59.4064%)
# Submitted  : 1787073808
# Exported   : 2026-08-18 17:27:58 UTC
#
# Hints: To find the longest sequential prefix, iterate from left to right. For a fixed <code>i</code>, if <code>nums[i] != nums[i - 1] + 1</code> then the longest sequential prefix ends at <code>i - 1</code>.
# ==========================================================
class Solution(object):
    def missingInteger(self, nums):
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                result += nums[i]
            else:
                break

        while result in nums:
            result += 1

        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        
