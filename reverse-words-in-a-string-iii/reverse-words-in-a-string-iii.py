# ==========================================================
# Problem    : Reverse Words in a String III
# URL        : https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String
#
# Acceptance : 84.0%
# Likes      : 6228  |  Dislikes: 256
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12728000  (beats 89.74820000000001%)
# Submitted  : 1777236961
# Exported   : 2026-04-26 21:06:17 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reverse_words = [word[::-1] for word in words]
        return " ".join(reverse_words)
        """
        :type s: str
        :rtype: str
        """
        
