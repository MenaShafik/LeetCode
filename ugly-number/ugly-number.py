# ==========================================================
# Problem    : Ugly Number
# URL        : https://leetcode.com/problems/ugly-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 43.5%
# Likes      : 3882  |  Dislikes: 1800
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12412000  (beats 17.795100000000005%)
# Submitted  : 1779610477
# Exported   : 2026-05-24 08:28:44 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        factor = [2,3,5]
        for i in factor:
            while n % i == 0 and n > 0:
                n //= i
        return n == 1
        """
        :type n: int
        :rtype: bool
        """
        
