# ==========================================================
# Problem    : Pascal's Triangle
# URL        : https://leetcode.com/problems/pascals-triangle/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Dynamic Programming
#
# Acceptance : 79.3%
# Likes      : 15159  |  Dislikes: 573
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12420000  (beats 26.93990000000001%)
# Submitted  : 1786784970
# Exported   : 2026-08-15 20:10:02 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            result .append(row)
        return result
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
