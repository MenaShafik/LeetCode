# ==========================================================
# Problem    : Smallest Divisible Digit Product I
# URL        : https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Enumeration
#
# Acceptance : 72.9%
# Likes      : 313  |  Dislikes: 20
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12508000  (beats 1.2658000000000058%)
# Submitted  : 1786003696
# Exported   : 2026-08-06 18:38:09 UTC
#
# Hints: You have to check at most 10 numbers.
#   Apply a brute-force approach by checking each possible number.
# ==========================================================
class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            product = 1
            temp = n

            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return n

            n += 1

        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
