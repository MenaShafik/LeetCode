# ==========================================================
# Problem    : Remove Outermost Parentheses
# URL        : https://leetcode.com/problems/remove-outermost-parentheses/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Stack
#
# Acceptance : 87.0%
# Likes      : 3788  |  Dislikes: 1725
#
# Language   : python
# Runtime    : 3  (beats 93.6658%)
# Memory     : 12356000  (beats 93.2615%)
# Submitted  : 1778883358
# Exported   : 2026-05-15 22:20:15 UTC
#
# Hints: Can you find the primitive decomposition?  The number of ( and ) characters must be equal.
# ==========================================================
class Solution(object):
    def removeOuterParentheses(self, s):
        stack = []
        result = []
        
        for char in s:
            if char == '(':
                if stack:
                    result.append(char)
                stack.append(char)
            else:  # char == ')'
                stack.pop()
                if stack:
                    result.append(char)
        
        return ''.join(result)  
            
        """
        :type s: str
        :rtype: str
        """
        
