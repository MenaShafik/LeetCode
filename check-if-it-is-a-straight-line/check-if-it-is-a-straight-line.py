# ==========================================================
# Problem    : Check If It Is a Straight Line
# URL        : https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Geometry
#
# Acceptance : 40.3%
# Likes      : 2712  |  Dislikes: 296
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12456000  (beats 90.90910000000001%)
# Submitted  : 1787044992
# Exported   : 2026-08-18 17:28:01 UTC
#
# Hints: If there're only 2 points, return true.
#   Check if all other points lie on the line defined by the first 2 points.
#   Use cross product to check collinearity.
# ==========================================================
class Solution(object):
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x, y in coordinates[2:]:
            if (y - y1) * (x2 - x1) != (y2 - y1) * (x - x1):
                return False

        return True
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
