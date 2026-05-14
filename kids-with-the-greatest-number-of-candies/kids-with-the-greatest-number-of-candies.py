# ==========================================================
# Problem    : Kids With the Greatest Number of Candies
# URL        : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 88.0%
# Likes      : 4978  |  Dislikes: 636
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12352000  (beats 54.59849999999999%)
# Submitted  : 1778752529
# Exported   : 2026-05-14 09:59:02 UTC
#
# Hints: For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i].
# ==========================================================
class Solution(object):
    def kidsWithCandies(self,candies,extraCandies):
        maxc=max(candies)
        result=[]
        for candy in candies:
            if candy+ extraCandies >= maxc:
                result.append(True)
            else:
                result.append(False)
        return result
              
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new = []
        for i in candies:
           new.append(i+extraCandies)
        for j in new:
            if j >= max(candies):
                new[new.index(j)] = True
            else:
                new[new.index(j)] = False
        return new
        """
        
