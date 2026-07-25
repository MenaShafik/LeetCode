# ==========================================================
# Problem    : Maximum Product of Two Digits
# URL        : https://leetcode.com/problems/maximum-product-of-two-digits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Sorting
#
# Acceptance : 75.6%
# Likes      : 289  |  Dislikes: 6
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12368000  (beats 58.5034%)
# Submitted  : 1785014074
# Exported   : 2026-07-25 22:42:29 UTC
#
# Hints: Use brute force
# ==========================================================
class Solution(object):
    def maxProduct(self, n):
        digits = [int(i) for i in str(n)]
        digits.sort(reverse=True)

        return digits[0] * digits[1]
        """
        :type n: int
        :rtype: int
        """
        
