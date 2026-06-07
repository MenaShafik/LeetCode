# ==========================================================
# Problem    : Valid Palindrome
# URL        : https://leetcode.com/problems/valid-palindrome/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 53.4%
# Likes      : 11751  |  Dislikes: 8650
#
# Language   : python
# Runtime    : 4  (beats 99.1795%)
# Memory     : 12824000  (beats 63.06649999999999%)
# Submitted  : 1780827198
# Exported   : 2026-06-07 10:22:45 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isPalindrome(self, s):
        p="!@#$%^&*(){}[]\_-:;,`.?'/\""
        s=s.replace(" ","")
        s=s.lower()
        for i in p:
            s=s.replace(i,"")
        return s==s[::-1]
        """
        :type s: str
        :rtype: bool
        """
        
