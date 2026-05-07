# ==========================================================
# Problem    : Valid Parentheses
# URL        : https://leetcode.com/problems/valid-parentheses/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Stack
#
# Acceptance : 44.1%
# Likes      : 28002  |  Dislikes: 2012
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12648000  (beats 11.044900000000002%)
# Submitted  : 1778152711
# Exported   : 2026-05-07 11:25:25 UTC
#
# Hints: Use a stack of characters.
#   When you encounter an opening bracket, push it to the top of the stack.
#   When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.
# ==========================================================
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

