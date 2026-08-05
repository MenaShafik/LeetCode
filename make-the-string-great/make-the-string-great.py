# ==========================================================
# Problem    : Make The String Great
# URL        : https://leetcode.com/problems/make-the-string-great/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Stack
#
# Acceptance : 68.6%
# Likes      : 3256  |  Dislikes: 190
#
# Language   : python
# Runtime    : 1  (beats 78.3459%)
# Memory     : 12464000  (beats 19.097699999999996%)
# Submitted  : 1785919808
# Exported   : 2026-08-05 18:29:34 UTC
#
# Hints: The order you choose 2 characters to remove doesn't matter.
#   Keep applying the mentioned step to s till the length of the string is not changed.
# ==========================================================
class Solution(object):
    def makeGood(self, s):
        stack=[]
        for char in s:
            if stack and stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        """
        :type s: str
        :rtype: str
        """
        
