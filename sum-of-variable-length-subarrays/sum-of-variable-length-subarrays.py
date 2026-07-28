# ==========================================================
# Problem    : Sum of Variable Length Subarrays
# URL        : https://leetcode.com/problems/sum-of-variable-length-subarrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Prefix Sum
#
# Acceptance : 85.9%
# Likes      : 122  |  Dislikes: 32
#
# Language   : python
# Runtime    : 3  (beats 95.7747%)
# Memory     : 12468000  (beats 16.901399999999995%)
# Submitted  : 1785229661
# Exported   : 2026-07-28 09:10:45 UTC
#
# Hints: The constraints are small, so brute force for each index.
# ==========================================================
class Solution(object):
    def subarraySum(self, nums):
        total = 0

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            total += sum(nums[start:i + 1])

        return total
        """
        :type nums: List[int]
        :rtype: int
        """
        
