# ==========================================================
# Problem    : Number of Strings That Appear as Substrings in Word
# URL        : https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# Acceptance : 82.5%
# Likes      : 759  |  Dislikes: 43
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12304000  (beats 59.420199999999994%)
# Submitted  : 1776807091
# Exported   : 2026-04-21 21:49:33 UTC
#
# Hints: Deal with each of the patterns individually.
#   Use the built-in function in the language you are using to find if the pattern exists as a substring in <code>word</code>.
# ==========================================================
class Solution(object):
    def numOfStrings(self, patterns, word):
        counter = 0
        for i in patterns:
            if i in word:
                counter+=1
        return counter

        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        
