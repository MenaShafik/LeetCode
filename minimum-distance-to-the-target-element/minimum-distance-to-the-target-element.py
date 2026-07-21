# ==========================================================
# Problem    : Minimum Distance to the Target Element
# URL        : https://leetcode.com/problems/minimum-distance-to-the-target-element/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 64.4%
# Likes      : 632  |  Dislikes: 86
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12560000  (beats 20.103099999999998%)
# Submitted  : 1784630460
# Exported   : 2026-07-21 10:42:51 UTC
#
# Hints: Loop in both directions until you find the target element.
#   For each index i such that nums[i] == target calculate abs(i - start).
# ==========================================================
class Solution(object):
    def getMinDistance(self, nums, target, start):
        min_distance = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                min_distance = min(min_distance, abs(i - start))
        return min_distance if min_distance != float('inf') else -1
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        
