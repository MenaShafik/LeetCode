# ==========================================================
# Problem    : Shift 2D Grid
# URL        : https://leetcode.com/problems/shift-2d-grid/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Matrix, Simulation
#
# Acceptance : 71.3%
# Likes      : 1905  |  Dislikes: 366
#
# Language   : python
# Runtime    : 3  (beats 81.0526%)
# Memory     : 12724000  (beats 15.7895%)
# Submitted  : 1784540529
# Exported   : 2026-07-20 09:56:54 UTC
#
# Hints: Simulate step by step. move grid[i][j] to grid[i][j+1]. handle last column of the grid.
#   Put the matrix row by row to a vector. take k % vector.length and move last k of the vector to the beginning. put the vector to the matrix back the same way.
# ==========================================================
class Solution(object):
    def shiftGrid(self, grid, k):
        arr = []

        rows = len(grid)
        cols = len(grid[0])

        k %= (rows * cols)

        # Flatten
        for i in range(rows):
            for j in range(cols):
                arr.append(grid[i][j])

        # Shift
        arr = arr[-k:] + arr[:-k]

        # Rebuild
        result = []
        for i in range(0, len(arr), cols):
            result.append(arr[i:i+cols])

        return result


        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
