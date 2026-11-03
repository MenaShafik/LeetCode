# ==========================================================
# Problem    : Minimum Moves to Equal Array Elements III
# URL        : https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 87.4%
# Likes      : 148  |  Dislikes: 6
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12092000  (beats 94.5945%)
# Submitted  : 1793697324
# Exported   : 2026-11-03 09:22:48 UTC
#
# Hints: To make all numbers equal, they must all reach at least the maximum value in the array.
# ==========================================================
class Solution(object):
    def minMoves(self, nums):
        counter = 0
        maxi = max(nums)

        for i in nums:
            counter += maxi - i

        return counter

        """
        :type nums: List[int]
        :rtype: int
        """
        
