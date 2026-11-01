# ==========================================================
# Problem    : Check If String Is a Prefix of Array
# URL        : https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, String
#
# Acceptance : 53.1%
# Likes      : 562  |  Dislikes: 110
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12072000  (beats 98.33340000000001%)
# Submitted  : 1793542760
# Exported   : 2026-11-01 22:55:17 UTC
#
# Hints: There are only words.length prefix strings.
#   Create all of them and see if s is one of them.
# ==========================================================
class Solution(object):
    def isPrefixString(self, s, words):
        stack = ''
        for i in words:
            stack+= i
            if stack == s:
                return True
        if len(stack) >len(s):
            return False
        return False
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
