# ================================================================
# Problem : Reverse String
# URL     : https://leetcode.com/problems/reverse-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# --- Community Stats ---
# Acceptance Rate : 80.7%
# Likes           : 9595
# Dislikes        : 1216
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 20452000  (beats 9.379800000000063%)
# Submitted  : 1773523038
#
# --- Hints ---
# The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
# ================================================================

class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp
        return s 
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
