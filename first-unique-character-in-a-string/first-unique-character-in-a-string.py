# ==========================================================
# Problem    : First Unique Character in a String
# URL        : https://leetcode.com/problems/first-unique-character-in-a-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Queue, Counting
#
# Acceptance : 65.8%
# Likes      : 9887  |  Dislikes: 336
#
# Language   : python
# Runtime    : 50  (beats 98.38529999999999%)
# Memory     : 12688000  (beats 74.7416%)
# Submitted  : 1783511487
# Exported   : 2026-07-08 11:53:29 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def firstUniqChar(self, s):
        result = ""
        for char in s:
            if char not in result:
                result += char
        for x in result:
            if s.count(x) == 1:
                return s.index(x)
        return -1
        """
        :type s: str
        :rtype: int
        """
        
