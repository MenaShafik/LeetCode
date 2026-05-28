# ==========================================================
# Problem    : Final Prices With a Special Discount in a Shop
# URL        : https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Stack, Monotonic Stack
#
# Acceptance : 84.1%
# Likes      : 2954  |  Dislikes: 156
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12332000  (beats 84.6056%)
# Submitted  : 1779958658
# Exported   : 2026-05-28 09:03:35 UTC
#
# Hints: Use brute force: For the ith item in the shop with a loop find the first position j satisfying the conditions and apply the discount, otherwise, the discount is 0.
# ==========================================================
class Solution(object):
    def finalPrices(self, prices):
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]

            stack.append(i)

        return prices

        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
