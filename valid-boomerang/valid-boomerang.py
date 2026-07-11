# ==========================================================
# Problem    : Valid Boomerang
# URL        : https://leetcode.com/problems/valid-boomerang/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Geometry
#
# Acceptance : 39.9%
# Likes      : 473  |  Dislikes: 544
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12408000  (beats 16.296300000000002%)
# Submitted  : 1783760681
# Exported   : 2026-07-11 09:14:52 UTC
#
# Hints: 3 points form a boomerang if and only if the triangle formed from them has non-zero area.
# ==========================================================
class Solution(object):
    def isBoomerang(self, points):
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
