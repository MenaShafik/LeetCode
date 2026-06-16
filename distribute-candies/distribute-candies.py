# ==========================================================
# Problem    : Distribute Candies
# URL        : https://leetcode.com/problems/distribute-candies/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 71.3%
# Likes      : 1758  |  Dislikes: 1490
#
# Language   : python
# Runtime    : 12  (beats 90.6205%)
# Memory     : 14012000  (beats 67.2439%)
# Submitted  : 1781603478
# Exported   : 2026-06-16 09:55:13 UTC
#
# Hints: To maximize the number of kinds of candies, we should try to distribute candies such that Alice will gain all kinds.
#   What is the upper limit of the number of kinds of candies Alice will gain? Remember candies are to distributed equally.
#   Which data structure is the most suitable for finding the number of kinds of candies?
#   Will hashset solves the problem? Inserting all candies kind in the hashset and then checking its size with upper limit.
# ==========================================================
class Solution(object):
    def distributeCandies(self, candyType):
        unique_candies = set(candyType)
        return min(len(unique_candies), len(candyType) // 2)
        """
        :type candyType: List[int]
        :rtype: int
        """
        
