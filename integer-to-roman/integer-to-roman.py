# ==========================================================
# Problem    : Integer to Roman
# URL        : https://leetcode.com/problems/integer-to-roman/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Hash Table, Math, String
#
# Acceptance : 71.2%
# Likes      : 8626  |  Dislikes: 5730
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12360000  (beats 56.18249999999999%)
# Submitted  : 1782808344
# Exported   : 2026-07-01 11:15:47 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        for i in range(len(val)):
            while num >= val[i]:
                roman_num += syms[i]
                num -= val[i]

        return roman_num        
        """
        :type num: int
        :rtype: str
        """
        
