# ==========================================================
# Problem    : Minimum Number Game
# URL        : https://leetcode.com/problems/minimum-number-game/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting, Heap (Priority Queue), Simulation
#
# Acceptance : 85.6%
# Likes      : 377  |  Dislikes: 27
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12304000  (beats 55.8095%)
# Submitted  : 1790754245
# Exported   : 2026-09-30 08:26:04 UTC
#
# Hints: Sort the array in increasing order and then swap the adjacent elements.
# ==========================================================
class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        stack = []
        for i in range(0,len(nums),2):
            stack.append(nums[i+1])
            stack.append(nums[i])
        return stack
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
