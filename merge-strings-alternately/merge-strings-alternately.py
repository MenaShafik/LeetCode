# ==========================================================
# Problem    : Merge Strings Alternately
# URL        : https://leetcode.com/problems/merge-strings-alternately/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 82.1%
# Likes      : 4949  |  Dislikes: 145
#
# Language   : python
# Runtime    : 12  (beats 84.8057%)
# Memory     : 12232000  (beats 92.1902%)
# Submitted  : 1776893608
# Exported   : 2026-04-22 21:45:30 UTC
#
# Hints: Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.
# ==========================================================
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        return result
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
