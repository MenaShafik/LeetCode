# ==========================================================
# Problem    : Count the Number of Special Characters I
# URL        : https://leetcode.com/problems/count-the-number-of-special-characters-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 74.3%
# Likes      : 302  |  Dislikes: 9
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12284000  (beats 92.6829%)
# Submitted  : 1779794378
# Exported   : 2026-05-26 11:31:03 UTC
#
# Hints: The constraints are small. For all 52 characters, check if they are present in <code>word</code>.
# ==========================================================
class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            elif ch.isupper():
                upper.add(ch.lower())

        return len(lower & upper)
        """
        :type word: str
        :rtype: int
        """
        
