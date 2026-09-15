# ==========================================================
# Problem    : N-th Tribonacci Number
# URL        : https://leetcode.com/problems/n-th-tribonacci-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Dynamic Programming, Memoization
#
# Acceptance : 63.0%
# Likes      : 4882  |  Dislikes: 214
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12292000  (beats 91.92060000000001%)
# Submitted  : 1789376837
# Exported   : 2026-09-15 10:59:04 UTC
#
# Hints: Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
#   Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].
# ==========================================================
class Solution(object):
    def tribonacci(self, n):
        count_sum = 0
        if n == 0:
            return 0
        if n == 1 and n == 2:
            return 1
        a = 0
        b = 1
        c = 1
        for i in range(3,n+1):
            count_sum =  a +b +c
            a = b
            b = c
            c = count_sum
            
        return c
        """
        :type n: int
        :rtype: int
        """
        
