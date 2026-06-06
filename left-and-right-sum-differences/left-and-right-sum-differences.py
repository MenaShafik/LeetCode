# ==========================================================
# Problem    : Left and Right Sum Differences
# URL        : https://leetcode.com/problems/left-and-right-sum-differences/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Prefix Sum
#
# Acceptance : 89.1%
# Likes      : 1380  |  Dislikes: 118
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12704000  (beats 18.50760000000001%)
# Submitted  : 1780739488
# Exported   : 2026-06-06 09:58:17 UTC
#
# Hints: For each index i, maintain two variables leftSum and rightSum.
#   Iterate on the range j: [0 … i - 1] and add nums[j] to the leftSum and similarly iterate on the range j: [i + 1 … nums.length - 1] and add nums[j] to the rightSum.
# ==========================================================
class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        left_sum = 0
        result = []

        for num in nums:
            total -= num
            result.append(abs(left_sum - total))
            left_sum += num

        return result
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
