# ================================================================
# Problem : Truncate Sentence
# URL     : https://leetcode.com/problems/truncate-sentence/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# --- Community Stats ---
# Acceptance Rate : 86.8%
# Likes           : 1231
# Dislikes        : 34
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12344000  (beats 68.2864%)
# Submitted  : 1775337393
#
# --- Hints ---
# It's easier to solve this problem on an array of strings so parse the string to an array of words
# After return the first k words as a sentence
# ================================================================

class Solution(object):
    def truncateSentence(self, s, k):
        word = s.split()
        for i in word:
            if len(word) >= k:
                return " ".join(word[:k])
            else:
                return s 

        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
