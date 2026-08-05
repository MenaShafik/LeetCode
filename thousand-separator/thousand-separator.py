# ==========================================================
# Problem    : Thousand Separator
# URL        : https://leetcode.com/problems/thousand-separator/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 53.8%
# Likes      : 523  |  Dislikes: 48
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12408000  (beats 15.90910000000001%)
# Submitted  : 1785954366
# Exported   : 2026-08-05 18:29:32 UTC
#
# Hints: Scan from the back of the integer and use dots to connect blocks with length 3 except the last block.
# ==========================================================
class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)
        ans = ""
        while len(s)>3:
            ans = "."+s[-3:] +ans
            s = s[:-3]
        return s+ ans
        """
        :type n: int
        :rtype: str
        """
        
