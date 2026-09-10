# ==========================================================
# Problem    : Lucky Numbers in a Matrix
# URL        : https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Matrix
#
# Acceptance : 80.3%
# Likes      : 2384  |  Dislikes: 124
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 23660000  (beats 1.818200000000001%)
# Submitted  : 1789026401
# Exported   : 2026-09-10 20:26:01 UTC
#
# Hints: Find out and save the minimum of each row and maximum of each column in two lists.
#   Then scan through the whole matrix to identify the elements that satisfy the criteria.
# ==========================================================
import numpy as np
class Solution(object):
    def luckyNumbers(self, matrix):
        min_in_rows = {min(row) for row in matrix}
        max_in_cols = {max(col) for col in zip(*matrix)}
        return list(min_in_rows & max_in_cols)
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
