# ================================================================
# Problem : Length of Last Word
# URL     : https://leetcode.com/problems/length-of-last-word/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# --- Community Stats ---
# Acceptance Rate : 58.7%
# Likes           : 6445
# Dislikes        : 365
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12568000  (beats 24.065199999999997%)
# Submitted  : 1772559724
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def lengthOfLastWord(self, s):

        words = s.split()
        return len(words[-1])
        """
        :type s: str
        :rtype: int
        """
        
