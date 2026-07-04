# ==========================================================
# Problem    : Fibonacci Number
# URL        : https://leetcode.com/problems/fibonacci-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Dynamic Programming, Recursion, Memoization
#
# Acceptance : 74.3%
# Likes      : 9437  |  Dislikes: 416
#
# Language   : python
# Runtime    : 7  (beats 98.34019999999998%)
# Memory     : 12396000  (beats 52.009299999999996%)
# Submitted  : 1783153518
# Exported   : 2026-07-04 08:27:08 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
            
        """
        :type n: int
        :rtype: int
        """
        
