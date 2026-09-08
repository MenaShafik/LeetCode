# ==========================================================
# Problem    : Check if Every Row and Column Contains All Numbers
# URL        : https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Matrix
#
# Acceptance : 54.3%
# Likes      : 1105  |  Dislikes: 58
#
# Language   : python
# Runtime    : 23  (beats 91.0%)
# Memory     : 12872000  (beats 19.0%)
# Submitted  : 1788768854
# Exported   : 2026-09-08 11:10:46 UTC
#
# Hints: Use for loops to check each row for every number from 1 to n. Similarly, do the same for each column.
#   For each check, you can keep a set of the unique elements in the checked row/col. By the end of the check, the size of the set should be n.
# ==========================================================
class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        expected = sorted(range(1,n+1))

        for i in matrix:
            if sorted(i) != expected:
                return False
        for col in zip(*matrix):
            if sorted(col) != expected:
                return False

        return True
        
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
