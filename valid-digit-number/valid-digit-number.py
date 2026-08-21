# ==========================================================
# Problem    : Valid Digit Number
# URL        : https://leetcode.com/problems/valid-digit-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 70.7%
# Likes      : 20  |  Dislikes: 0
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12252000  (beats 90.1786%)
# Submitted  : 1787342920
# Exported   : 2026-08-21 21:52:24 UTC
#
# Hints: Perform the checks as described
# ==========================================================
class Solution(object):
    def validDigit(self, n, x):
        str_n = str(n)

        for i in range(len(str_n)):
            if str_n[i] == str(x) and str_n[0] != str(x):
                return True

        return False
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        
