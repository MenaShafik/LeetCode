# ==========================================================
# Problem    : Check if the Sentence Is Pangram
# URL        : https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 84.3%
# Likes      : 3049  |  Dislikes: 67
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12308000  (beats 54.11939999999999%)
# Submitted  : 1785142295
# Exported   : 2026-07-27 08:55:23 UTC
#
# Hints: Iterate over the string and mark each character as found (using a boolean array, bitmask, or any other similar way).
#   Check if the number of found characters equals the alphabet length.
# ==========================================================
class Solution(object):
    def checkIfPangram(self, sentence):
        import string

        for c in string.ascii_lowercase:
            if c not in sentence:
                return False
        return True

        """
        :type sentence: str
        :rtype: bool
        """
        
