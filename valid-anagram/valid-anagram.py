# ==========================================================
# Problem    : Valid Anagram
# URL        : https://leetcode.com/problems/valid-anagram/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Sorting
#
# Acceptance : 68.2%
# Likes      : 14447  |  Dislikes: 481
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12616000  (beats 49.6233%)
# Submitted  : 1780917755
# Exported   : 2026-06-08 11:24:36 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def isAnagram(self, s, t):
        strings = "abcdefghijklmnopqrstuvwxyz"
        for i in strings:
            if s.count(i) != t.count(i):
                return False
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
