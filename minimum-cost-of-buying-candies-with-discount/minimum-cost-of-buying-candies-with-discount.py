# ==========================================================
# Problem    : Minimum Cost of Buying Candies With Discount
# URL        : https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Greedy, Sorting
#
# Acceptance : 67.9%
# Likes      : 806  |  Dislikes: 28
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12460000  (beats 18.750100000000003%)
# Submitted  : 1780302846
# Exported   : 2026-06-01 08:56:21 UTC
#
# Hints: If we consider costs from high to low, what is the maximum cost of a single candy that we can get for free?
#   How can we generalize this approach to maximize the costs of the candies we get for free?
#   Can “sorting” the array help us find the minimum cost?
# ==========================================================
class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total = 0
        for i in range(0, len(cost),3):
            total+=cost[i]
            if i+ 1 < len(cost):
                total+= cost[i+1]
        return total
        """
        :type cost: List[int]
        :rtype: int
        """
        
