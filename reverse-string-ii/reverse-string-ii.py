# ==========================================================
# Problem    : Reverse String II
# URL        : https://leetcode.com/problems/reverse-string-ii/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 54.0%
# Likes      : 2398  |  Dislikes: 4497
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12644000  (beats 42.456100000000006%)
# Submitted  : 1783247203
# Exported   : 2026-07-05 10:29:46 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0,len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)

        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
