# ==========================================================
# Problem    : Maximum Number of Words You Can Type
# URL        : https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 82.9%
# Likes      : 997  |  Dislikes: 40
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12604000  (beats 3.6584000000000003%)
# Submitted  : 1776541209
# Exported   : 2026-04-18 19:41:33 UTC
#
# Hints: Check each word separately if it can be typed.
#   A word can be typed if all its letters are not broken.
# ==========================================================
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        brokenLetters = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(letter in brokenLetters for letter in word):
                count += 1 
        return count
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
