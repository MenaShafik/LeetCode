# ================================================================
# Problem : To Lower Case
# URL     : https://leetcode.com/problems/to-lower-case/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# --- Community Stats ---
# Acceptance Rate : 84.8%
# Likes           : 2049
# Dislikes        : 2800
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12272000  (beats 92.9952%)
# Submitted  : 1773951989
#
# --- Hints ---
# Most languages support lowercase conversion for a string data type. However, that is certainly not the purpose of the problem. Think about how the implementation of the lowercase function call can be done easily.
# <b>Think ASCII!</b>
# Think about the different capital letters and their ASCII codes and how that relates to their lowercase counterparts. Does there seem to be any pattern there? Any mathematical relationship that we can use?
# ================================================================

class Solution(object):
    def toLowerCase(self, s):
        return s.lower()
        """
        :type s: str
        :rtype: str
        """
        
