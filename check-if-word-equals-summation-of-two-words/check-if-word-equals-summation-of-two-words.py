# ==========================================================
# Problem    : Check if Word Equals Summation of Two Words
# URL        : https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 75.5%
# Likes      : 616  |  Dislikes: 42
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12108000  (beats 100.0%)
# Submitted  : 1792220733
# Exported   : 2026-10-17 07:20:21 UTC
#
# Hints: Convert each character of each word to its numerical value.
#   Check if the numerical values satisfies the condition.
# ==========================================================

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        word1 = ""
        word2 = ""
        word3 = ""

        for i in firstWord:
            word1 += str(ord(i) - ord('a'))

        for j in secondWord:
            word2 += str(ord(j) - ord('a'))

        for s in targetWord:
            word3 += str(ord(s) - ord('a'))

        return int(word1) + int(word2) == int(word3)


        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        
