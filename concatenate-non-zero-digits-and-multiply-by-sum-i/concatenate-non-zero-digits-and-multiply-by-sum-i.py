# ==========================================================
# Problem    : Concatenate Non-Zero Digits and Multiply by Sum I
# URL        : https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 66.2%
# Likes      : 265  |  Dislikes: 3
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12348000  (beats 54.86309999999999%)
# Submitted  : 1785057269
# Exported   : 2026-07-27 08:55:29 UTC
#
# Hints: Simulate as described
# ==========================================================
class Solution(object):
    def sumAndMultiply(self, n):
        value = 0
        string = str(n).replace("0", "")
        for i in string:
            value+= int(i)
        return (int(string) if string else 0) * value
        """
        :type n: int
        :rtype: int
        """
        
