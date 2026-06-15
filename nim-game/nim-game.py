# ==========================================================
# Problem    : Nim Game
# URL        : https://leetcode.com/problems/nim-game/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Brainteaser, Game Theory
#
# Acceptance : 59.9%
# Likes      : 2038  |  Dislikes: 2753
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12456000  (beats 16.85389999999999%)
# Submitted  : 1781515638
# Exported   : 2026-06-15 09:39:54 UTC
#
# Hints: If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?
# ==========================================================
class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0
        
        """
        :type n: int
        :rtype: bool
        """
        
