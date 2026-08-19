# ==========================================================
# Problem    : Largest Even Number
# URL        : https://leetcode.com/problems/largest-even-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 69.3%
# Likes      : 74  |  Dislikes: 1
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12344000  (beats 59.63850000000001%)
# Submitted  : 1787132727
# Exported   : 2026-08-19 19:55:51 UTC
#
# Hints: A number ending with <code>'1'</code> is odd.
#   Find the last <code>'2'</code> in <code>s</code>. If none, return <code>""</code>. Otherwise return the prefix up to and including that <code>'2'</code>.
# ==========================================================
class Solution(object):
    def largestEven(self, s):
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 0:
                return s[:i + 1]

        return ""
        """
        :type s: str
        :rtype: str
        """
        
