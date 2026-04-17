# ================================================================
# Problem : Reverse Prefix of Word
# URL     : https://leetcode.com/problems/reverse-prefix-of-word/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String, Stack
#
# --- Community Stats ---
# Acceptance Rate : 86.5%
# Likes           : 1523
# Dislikes        : 46
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12344000  (beats 64.8231%)
# Submitted  : 1775852694
#
# --- Hints ---
# Find the first index where ch appears.
# Find a way to reverse a substring of word.
# ================================================================

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        test=[]
        for i in word:
            test.append(i)
            if i == ch:
                return ''.join(test[::-1]) + word[len(test):]
        return word

