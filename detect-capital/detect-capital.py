# ==========================================================
# Problem    : Detect Capital
# URL        : https://leetcode.com/problems/detect-capital/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 56.7%
# Likes      : 3615  |  Dislikes: 473
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12368000  (beats 50.691700000000004%)
# Submitted  : 1781685390
# Exported   : 2026-06-17 08:54:00 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True
        return False
        """
        :type word: str
        :rtype: bool
        """
        
