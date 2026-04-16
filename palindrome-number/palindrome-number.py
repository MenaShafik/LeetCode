# ================================================================
# Problem : Palindrome Number
# URL     : https://leetcode.com/problems/palindrome-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 60.5%
# Likes           : 15962
# Dislikes        : 2936
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12400000  (beats 62.38319999999999%)
# Submitted  : 1769279510
#
# --- Hints ---
# Beware of overflow when you reverse the integer.
# ================================================================

class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        if a==a[::-1]:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
        
