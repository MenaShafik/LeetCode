# ==========================================================
# Problem    : Backspace String Compare
# URL        : https://leetcode.com/problems/backspace-string-compare/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Two Pointers, String, Stack, Simulation
#
# Acceptance : 50.0%
# Likes      : 7993  |  Dislikes: 386
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12484000  (beats 19.4274%)
# Submitted  : 1782745372
# Exported   : 2026-06-29 15:13:52 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def backspaceCompare(self, s, t):
        def process(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)

        return process(s) == process(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
