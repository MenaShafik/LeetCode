# ==========================================================
# Problem    : Arranging Coins
# URL        : https://leetcode.com/problems/arranging-coins/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Binary Search
#
# Acceptance : 48.3%
# Likes      : 4370  |  Dislikes: 1381
#
# Language   : python
# Runtime    : 407  (beats 34.57829999999995%)
# Memory     : 12420000  (beats 17.842200000000012%)
# Submitted  : 1781439369
# Exported   : 2026-06-14 12:34:02 UTC
#
# Hints: N/A
# ==========================================================
class Solution:
    def arrangeCoins(self, n):
        row = 1
        while n >= row:
            n -= row
            row += 1
        return row - 1
        """
        :type n: int
        :rtype: int
        """
        
