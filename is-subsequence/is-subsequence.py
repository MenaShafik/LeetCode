# ==========================================================
# Problem    : Is Subsequence
# URL        : https://leetcode.com/problems/is-subsequence/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String, Dynamic Programming
#
# Acceptance : 49.2%
# Likes      : 10899  |  Dislikes: 622
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12428000  (beats 46.60440000000001%)
# Submitted  : 1783246948
# Exported   : 2026-07-05 10:29:47 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isSubsequence(self, s, t):
        s_index = 0
        t_index = 0
        while  s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index+= 1 
            t_index += 1
        return s_index == len(s)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
