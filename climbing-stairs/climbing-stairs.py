# ==========================================================
# Problem    : Climbing Stairs
# URL        : https://leetcode.com/problems/climbing-stairs/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Dynamic Programming, Memoization
#
# Acceptance : 54.1%
# Likes      : 24608  |  Dislikes: 1050
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12436000  (beats 20.061300000000003%)
# Submitted  : 1780917141
# Exported   : 2026-06-08 11:24:39 UTC
#
# Hints: To reach nth step, what could have been your previous steps? (Think about the step sizes)
# ==========================================================
class Solution(object):
    def climbStairs(self, n):
        count,step = 1,1
        
        for _ in range(n):
            count, step = step, count + step
        return count
        """
        :type n: int
        :rtype: int
        """
        
