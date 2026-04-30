# ==========================================================
# Problem    : First Letter to Appear Twice
# URL        : https://leetcode.com/problems/first-letter-to-appear-twice/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Bit Manipulation, Counting
#
# Acceptance : 75.0%
# Likes      : 1192  |  Dislikes: 65
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12256000  (beats 86.68480000000001%)
# Submitted  : 1777577341
# Exported   : 2026-04-30 19:44:32 UTC
#
# Hints: Iterate through the string from left to right. Keep track of the elements you have already seen in a set.
#   If the current element is already in the set, return that element.
# ==========================================================
class Solution(object):
    def repeatedCharacter(self, s):
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return None
        """
        :type s: str
        :rtype: str
        """
        
