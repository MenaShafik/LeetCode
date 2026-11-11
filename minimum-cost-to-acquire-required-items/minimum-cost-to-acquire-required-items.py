# ==========================================================
# Problem    : Minimum Cost to Acquire Required Items
# URL        : https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Math, Greedy
#
# Acceptance : 45.7%
# Likes      : 159  |  Dislikes: 17
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12224000  (beats 41.6667%)
# Submitted  : 1794386829
# Exported   : 2026-11-11 08:52:36 UTC
#
# Hints: First, use <code>min(costBoth, cost1 + cost2)</code> for <code>min(need1, need2)</code>.
#   For the remaining type 1 requirement <code>rem1</code>, use cost <code>min(costBoth, cost1)</code> for the rest.
#   Do the same for type 2, using cost <code>min(costBoth, cost2)</code>.
# ==========================================================
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        option1 = cost1 * need1 + cost2 * need2
        option2 = min(need1, need2) * costBoth
        option2 += (need1 - min(need1,need2))* cost1
        option2 += (need2 - min(need1,need2))* cost2
        option3 = max(need1,need2) * costBoth
        return min(option1,option2,option3)

        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        
