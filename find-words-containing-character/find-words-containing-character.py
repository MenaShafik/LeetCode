# ================================================================
# Problem : Find Words Containing Character
# URL     : https://leetcode.com/problems/find-words-containing-character/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# --- Community Stats ---
# Acceptance Rate : 90.4%
# Likes           : 705
# Dislikes        : 55
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12420000  (beats 26.645100000000006%)
# Submitted  : 1774984376
#
# --- Hints ---
# Use two nested loops.
# ================================================================

class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        return result
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        
