# ==========================================================
# Problem    : Excel Sheet Column Title
# URL        : https://leetcode.com/problems/excel-sheet-column-title/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 46.8%
# Likes      : 6100  |  Dislikes: 926
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12388000  (beats 54.6929%)
# Submitted  : 1783153204
# Exported   : 2026-07-04 08:27:10 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))

        """
        :type columnNumber: int
        :rtype: str
        """
        
