# ==========================================================
# Problem    : Stone Removal Game
# URL        : https://leetcode.com/problems/stone-removal-game/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Simulation
#
# Acceptance : 53.5%
# Likes      : 226  |  Dislikes: 10
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12000000  (beats 100.0%)
# Submitted  : 1795681577
# Exported   : 2026-11-26 15:49:28 UTC
#
# Hints: The constraints are small enough that a brute-force solution is feasible.
# ==========================================================
class Solution(object):
    def canAliceWin(self, n):
        stones = 10
        alice = True

        while n >= stones:
            n -= stones
            stones -= 1
            alice = not alice

        return not alice

        """
        :type n: int
        :rtype: bool
        """
        
