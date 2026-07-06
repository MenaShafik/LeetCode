# ==========================================================
# Problem    : Construct the Rectangle
# URL        : https://leetcode.com/problems/construct-the-rectangle/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 64.1%
# Likes      : 805  |  Dislikes: 394
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12280000  (beats 91.4893%)
# Submitted  : 1783329625
# Exported   : 2026-07-06 09:38:01 UTC
#
# Hints: The W is always less than or equal to the square root of the area, so we start searching at sqrt(area) till we find the result.
# ==========================================================
class Solution(object):
    def constructRectangle(self, area):
        w = int(area ** 0.5) 
        # w = 2 
        while area % w !=0:
            w-=1
        l  = area // w
        return [l,w]
        """
        :type area: int
        :rtype: List[int]
        """
        
