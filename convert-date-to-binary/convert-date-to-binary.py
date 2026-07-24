# ==========================================================
# Problem    : Convert Date to Binary
# URL        : https://leetcode.com/problems/convert-date-to-binary/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 88.5%
# Likes      : 162  |  Dislikes: 11
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12464000  (beats 16.878999999999998%)
# Submitted  : 1784804066
# Exported   : 2026-07-24 13:18:52 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def convertDateToBinary(self, date):
        year, month, day = date.split("-")

        return bin(int(year))[2:] + "-" + bin(int(month))[2:] + "-" + bin(int(day))[2:]
        """
        :type date: str
        :rtype: str
        """
        
