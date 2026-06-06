# ==========================================================
# Problem    : Best Time to Buy and Sell Stock
# URL        : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Dynamic Programming
#
# Acceptance : 56.9%
# Likes      : 35872  |  Dislikes: 1425
#
# Language   : python
# Runtime    : 22  (beats 99.04440000000001%)
# Memory     : 19116000  (beats 37.7141%)
# Submitted  : 1780678288
# Exported   : 2026-06-06 09:58:19 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        profit = 0
        for day in prices:
            if day < min_price:
                min_price = day
            if day - min_price > profit:
                profit = day - min_price
        return profit
            
            
            

        """
        :type prices: List[int]
        :rtype: int
        """
        
