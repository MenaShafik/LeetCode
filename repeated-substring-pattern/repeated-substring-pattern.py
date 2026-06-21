# ==========================================================
# Problem    : Repeated Substring Pattern
# URL        : https://leetcode.com/problems/repeated-substring-pattern/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, String Matching
#
# Acceptance : 48.4%
# Likes      : 6897  |  Dislikes: 571
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12456000  (beats 83.5415%)
# Submitted  : 1782034525
# Exported   : 2026-06-21 09:45:21 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def repeatedSubstringPattern(self, s):
        a=s+s
        a=a[1:-1]
        if s in a:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        
