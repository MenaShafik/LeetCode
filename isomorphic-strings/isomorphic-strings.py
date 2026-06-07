# ==========================================================
# Problem    : Isomorphic Strings
# URL        : https://leetcode.com/problems/isomorphic-strings/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 48.5%
# Likes      : 10637  |  Dislikes: 2290
#
# Language   : python
# Runtime    : 6  (beats 92.45909999999999%)
# Memory     : 15116000  (beats 12.145499999999993%)
# Submitted  : 1780827662
# Exported   : 2026-06-07 10:22:43 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(s))==len(set(t))==len(set(zip(s,t)))


        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
