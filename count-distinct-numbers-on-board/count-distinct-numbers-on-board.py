# ==========================================================
# Problem    : Count Distinct Numbers on Board
# URL        : https://leetcode.com/problems/count-distinct-numbers-on-board/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Math, Simulation
#
# Acceptance : 62.0%
# Likes      : 325  |  Dislikes: 296
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12244000  (beats 86.95649999999999%)
# Submitted  : 1789548294
# Exported   : 2026-09-16 09:00:43 UTC
#
# Hints: For n > 2, n % (n - 1) == 1 thus n - 1 will be added on the board the next day.
#   As the operations are performed for so long time, all the numbers lesser than n except 1 will be added to the board.
#   What will happen if n == 1?
# ==========================================================
class Solution(object):
    def distinctIntegers(self, n):
        if n ==1:
            return 1
        return n-1
        """
        :type n: int
        :rtype: int
        """
        
