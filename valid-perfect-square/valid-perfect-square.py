# ==========================================================
# Problem    : Valid Perfect Square
# URL        : https://leetcode.com/problems/valid-perfect-square/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Binary Search
#
# Acceptance : 45.0%
# Likes      : 4694  |  Dislikes: 338
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12324000  (beats 55.806000000000004%)
# Submitted  : 1781382703
# Exported   : 2026-06-13 20:38:00 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isPerfectSquare(self, num):
        if num >= 0:
            x = int(num ** 0.5)
            if pow(x, 2) == num:
                return True
        return False
        """
        :type num: int
        :rtype: bool
        """
        
