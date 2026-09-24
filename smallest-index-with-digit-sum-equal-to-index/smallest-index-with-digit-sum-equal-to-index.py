# ==========================================================
# Problem    : Smallest Index With Digit Sum Equal to Index
# URL        : https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 83.6%
# Likes      : 191  |  Dislikes: 8
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12316000  (beats 61.594200000000015%)
# Submitted  : 1790238283
# Exported   : 2026-09-24 11:50:46 UTC
#
# Hints: Simulate as described
# ==========================================================
class Solution(object):
    def smallestIndex(self, nums):

        for i in range(len(nums)):

            counter = 0

            for j in str(nums[i]):
                counter+=int(j)

            if counter == i:
                return i

        return -1

            
        """
        :type nums: List[int]
        :rtype: int
        """
        
