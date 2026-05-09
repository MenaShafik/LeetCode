# ==========================================================
# Problem    : Find the Degree of Each Vertex
# URL        : https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : N/A
#
# Acceptance : 92.7%
# Likes      : 36  |  Dislikes: 0
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12532000  (beats 83.2465%)
# Submitted  : 1778323638
# Exported   : 2026-05-09 10:53:45 UTC
#
# Hints: The degree of node <code>i</code> is the sum of row <code>i</code> in the matrix
# ==========================================================
class Solution(object):
    def findDegrees(self, matrix):
        return [sum(value) for value in matrix]
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
