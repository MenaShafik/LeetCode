# ==========================================================
# Problem    : Count Negative Numbers in a Sorted Matrix
# URL        : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Binary Search, Matrix
#
# Acceptance : 79.7%
# Likes      : 5534  |  Dislikes: 147
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13188000  (beats 67.93249999999999%)
# Submitted  : 1787733829
# Exported   : 2026-08-26 18:21:00 UTC
#
# Hints: Use binary search for optimization or simply brute force.
# ==========================================================
class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count+=1
        return count
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
