# ==========================================================
# Problem    : Check Divisibility by Digit Sum and Product
# URL        : https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 74.6%
# Likes      : 270  |  Dislikes: 6
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12432000  (beats 13.696599999999997%)
# Submitted  : 1787390368
# Exported   : 2026-08-23 21:47:17 UTC
#
# Hints: Compute the digits' sum and product, then check if <code>n % (sum + product) == 0</code>.
# ==========================================================
class Solution(object):
    def checkDivisibility(self, n):
        str_n = str(n)
        sum_n=0
        product_n=1
        for i in str_n:
            i = int(i)
            sum_n+=i
            product_n *= i
        if n % (sum_n + product_n) == 0:
            return True
        else:
            return False
        
        """
        :type n: int
        :rtype: bool
        """
        
