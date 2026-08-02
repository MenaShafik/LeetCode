# ==========================================================
# Problem    : Three Divisors
# URL        : https://leetcode.com/problems/three-divisors/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Enumeration, Number Theory
#
# Acceptance : 64.6%
# Likes      : 647  |  Dislikes: 37
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12648000  (beats 49.768400000000014%)
# Submitted  : 1785618018
# Exported   : 2026-08-02 16:15:41 UTC
#
# Hints: You can count the number of divisors and just check that they are 3
#   Beware of the case of n equal 1 as some solutions might fail in it
# ==========================================================
class Solution(object):
    def isThree(self, n):
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count+=1
        if count == 3:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        
