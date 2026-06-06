# ==========================================================
# Problem    : Excel Sheet Column Number
# URL        : https://leetcode.com/problems/excel-sheet-column-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 67.8%
# Likes      : 5116  |  Dislikes: 403
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12344000  (beats 51.75870000000001%)
# Submitted  : 1780739739
# Exported   : 2026-06-06 09:58:14 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
        """
        :type columnTitle: str
        :rtype: int
        """
        
