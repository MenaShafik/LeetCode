# ==========================================================
# Problem    : Maximum Average Subarray I
# URL        : https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sliding Window
#
# Acceptance : 48.4%
# Likes      : 4497  |  Dislikes: 387
#
# Language   : python
# Runtime    : 75  (beats 71.2973%)
# Memory     : 19036000  (beats 49.8609%)
# Submitted  : 1783849588
# Exported   : 2026-07-12 09:48:45 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum = sum(nums[:k])
        current_sum = max_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        return (float(max_sum) / k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
