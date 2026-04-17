# ================================================================
# Problem : Subtract the Product and Sum of Digits of an Integer
# URL     : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 86.6%
# Likes           : 2840
# Dislikes        : 255
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12384000  (beats 59.2948%)
# Submitted  : 1775769354
#
# --- Hints ---
# How to compute all digits of the number ?
# Use modulus operator (%) to compute the last digit.
# Generalise modulus operator idea to compute all digits.
# ================================================================

class Solution(object):
    def subtractProductAndSum(self, n):
        sums = 0
        product=1
        for i in str(n):
            sums+=int(i)
            product*=int(i)
        return product - sums
        """
        :type n: int
        :rtype: int
        """
        
