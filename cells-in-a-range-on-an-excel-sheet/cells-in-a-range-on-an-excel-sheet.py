# ==========================================================
# Problem    : Cells in a Range on an Excel Sheet
# URL        : https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 84.1%
# Likes      : 655  |  Dislikes: 100
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12452000  (beats 24.242399999999996%)
# Submitted  : 1785323305
# Exported   : 2026-07-29 11:55:00 UTC
#
# Hints: From the given string, find the corresponding rows and columns.
#   Iterate through the columns in ascending order and for each column, iterate through the rows in ascending order to obtain the required cells in sorted order.
# ==========================================================
class Solution(object):
    def cellsInRange(self, s):
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        start_column = s[0]
        start_row = int(s[1])
        end_column = s[3]
        end_row = int(s[4])

        start_index = abc.index(start_column)
        end_index = abc.index(end_column)

        result = []

        for c in range(start_index, end_index + 1):
            for r in range(start_row, end_row + 1):
                result.append(abc[c] + str(r))

        return result
            



        """
        :type s: str
        :rtype: List[str]
        """
        
