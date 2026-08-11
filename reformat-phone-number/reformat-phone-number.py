# ==========================================================
# Problem    : Reformat Phone Number
# URL        : https://leetcode.com/problems/reformat-phone-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 67.8%
# Likes      : 404  |  Dislikes: 206
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12520000  (beats 1.6393999999999895%)
# Submitted  : 1786438129
# Exported   : 2026-08-11 21:07:11 UTC
#
# Hints: Discard all the spaces and dashes.
#   Use a while loop. While the string still has digits, check its length and see which rule to apply.
# ==========================================================
class Solution(object):
    def reformatNumber(self, number):
        number = number.replace(" ", "").replace("-", "")

        result = ""
        i = 0

        while len(number) - i > 4:
            result += number[i:i+3] + "-"
            i += 3

        remaining = number[i:]

        if len(remaining) == 4:
            result += remaining[:2] + "-" + remaining[2:]
        else:
            result += remaining

        return result
            

        """
        :type number: str
        :rtype: str
        """
        
