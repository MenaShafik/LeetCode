# ==========================================================
# Problem    : String Matching in an Array
# URL        : https://leetcode.com/problems/string-matching-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String, String Matching
#
# Acceptance : 69.8%
# Likes      : 1514  |  Dislikes: 131
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12264000  (beats 91.5301%)
# Submitted  : 1786220358
# Exported   : 2026-08-08 21:55:06 UTC
#
# Hints: Bruteforce to find if one string is substring of another or use KMP algorithm.
# ==========================================================
class Solution(object):
    def stringMatching(self, words):
        stack = []
        for word_1 in range(len(words)):
            for word_2 in range(len(words)):
                if word_1!= word_2 and words[word_1] in words[word_2]:
                    stack.append(words[word_1])
                    break
        return stack
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
