# ==========================================================
# Problem    : Count Primes
# URL        : https://leetcode.com/problems/count-primes/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Math, Enumeration, Number Theory
#
# Acceptance : 36.1%
# Likes      : 8866  |  Dislikes: 1582
#
# Language   : python
# Runtime    : 2449  (beats 74.78919999999925%)
# Memory     : 130788000  (beats 30.76919999999993%)
# Submitted  : 1780131248
# Exported   : 2026-05-30 08:56:15 UTC
#
# Hints: Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
#   Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
#   Use Sieve of Eratosthenes.
# ==========================================================
class Solution(object):
    def countPrimes(self, n):
        if n <=2:
            return 0
        is_prime  = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
        """
        :type n: int
        :rtype: int
        """
        
