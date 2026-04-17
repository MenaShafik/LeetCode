# ================================================================
# Problem : Check If Two String Arrays are Equivalent
# URL     : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, String
#
# --- Community Stats ---
# Acceptance Rate : 86.1%
# Likes           : 3163
# Dislikes        : 205
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12488000  (beats 43.7134%)
# Submitted  : 1773772803
#
# --- Hints ---
# Concatenate all strings in the first array into a single string in the given order, the same for the second array.
# Both arrays represent the same string if and only if the generated strings are the same.
# ================================================================

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)

