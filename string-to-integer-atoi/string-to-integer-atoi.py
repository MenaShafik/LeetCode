# ==========================================================
# Problem    : String to Integer (atoi)
# URL        : https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 21.5%
# Likes      : 6388  |  Dislikes: 15782
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12276000  (beats 92.0809%)
# Submitted  : 1786177568
# Exported   : 2026-08-08 21:55:09 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        result = sign * result
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result

        """
        :type s: str
        :rtype: int
        """
        
