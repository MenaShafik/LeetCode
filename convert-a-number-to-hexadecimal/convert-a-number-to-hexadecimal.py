# ==========================================================
# Problem    : Convert a Number to Hexadecimal
# URL        : https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Bit Manipulation
#
# Acceptance : 54.5%
# Likes      : 1452  |  Dislikes: 232
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12376000  (beats 53.01650000000001%)
# Submitted  : 1783933473
# Exported   : 2026-07-13 09:21:07 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        digits = "0123456789abcdef"
        num &= 0xffffffff
        result = ""


        while num:
            result = digits[num & 15] + result
            num >>= 4

        return result
        """
        :type num: int
        :rtype: str
        """
        
