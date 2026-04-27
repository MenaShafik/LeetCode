# ==========================================================
# Problem    : Calculate Money in Leetcode Bank
# URL        : https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 82.3%
# Likes      : 1847  |  Dislikes: 64
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12408000  (beats 18.542899999999996%)
# Submitted  : 1777318030
# Exported   : 2026-04-27 19:31:20 UTC
#
# Hints: Simulate the process by keeping track of how much money Hercy is putting in and which day of the week it is, and use this information to deduce how much money Hercy will put in the next day.
# ==========================================================
class Solution(object):
    def totalMoney(self, n):
        mn = 0
        for i in range(0,n):
            mn+= (i//7 + 1) + (i%7)
        return mn
        """
        :type n: int
        :rtype: int
        """
        
