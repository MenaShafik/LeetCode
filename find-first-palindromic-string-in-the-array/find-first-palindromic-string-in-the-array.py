# ==========================================================
# Problem    : Find First Palindromic String in the Array
# URL        : https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, String
#
# Acceptance : 84.1%
# Likes      : 1683  |  Dislikes: 61
#
# Language   : python
# Runtime    : 2  (beats 68.5272%)
# Memory     : 12228000  (beats 93.3334%)
# Submitted  : 1792913524
# Exported   : 2026-10-25 12:08:05 UTC
#
# Hints: Iterate through the elements in order. As soon as the current element is a palindrome, return it.
#   To check if an element is a palindrome, can you reverse the string?
# ==========================================================
class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if i == i[::-1]:
                return i
        return ""
        
        """
        :type words: List[str]
        :rtype: str
        """
        
