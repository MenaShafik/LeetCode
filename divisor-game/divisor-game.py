# ==========================================================
# Problem    : Divisor Game
# URL        : https://leetcode.com/problems/divisor-game/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Dynamic Programming, Brainteaser, Game Theory
#
# Acceptance : 72.0%
# Likes      : 2460  |  Dislikes: 4212
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12288000  (beats 88.91050000000001%)
# Submitted  : 1782124152
# Exported   : 2026-06-22 10:32:20 UTC
#
# Hints: If the current number is even, we can always subtract a 1 to make it odd.  If the current number is odd, we must subtract an odd number to make it even.
# ==========================================================
class Solution(object):
    def divisorGame(self, n):
        while n > 0:
            return n % 2 == 0
        """
        :type n: int
        :rtype: bool
        """
        
