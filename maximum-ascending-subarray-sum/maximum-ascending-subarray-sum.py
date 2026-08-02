# ==========================================================
# Problem    : Maximum Ascending Subarray Sum
# URL        : https://leetcode.com/problems/maximum-ascending-subarray-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 66.3%
# Likes      : 1305  |  Dislikes: 44
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12336000  (beats 55.0633%)
# Submitted  : 1785666232
# Exported   : 2026-08-02 16:15:39 UTC
#
# Hints: It is fast enough to check all possible subarrays
#   The end of each ascending subarray will be the start of the next
# ==========================================================
class Solution(object):
    def maxAscendingSum(self, nums):
        stack = [nums[0]]
        max_num = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                stack.append(nums[i])
            else:
                max_num = max(max_num,sum(stack))
                stack = [nums[i]]
        max_num = max(max_num,sum(stack))
        return max_num

        """
        :type nums: List[int]
        :rtype: int
        """
        
