# ==========================================================
# Problem    : Min Max Game
# URL        : https://leetcode.com/problems/min-max-game/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# Acceptance : 64.6%
# Likes      : 600  |  Dislikes: 34
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12348000  (beats 63.15789999999999%)
# Submitted  : 1794989290
# Exported   : 2026-11-18 11:39:56 UTC
#
# Hints: Simply simulate the algorithm.
#   Note that the size of the array decreases exponentially, so the process will terminate after just O(log n) steps.
# ==========================================================
class Solution(object):
    def minMaxGame(self, nums):
        while len(nums) > 1:
            stack = []
            for i in range(len(nums)//2):
                if i %2 ==0:
                    stack.append(min(nums[2*i], nums[2*i+1]))
                else:
                    stack.append(max(nums[2*i], nums[2*i+1]))
            nums = stack
        return nums[0]


        """
        :type nums: List[int]
        :rtype: int
        """
        
