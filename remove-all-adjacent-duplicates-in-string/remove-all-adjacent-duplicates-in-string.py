# ==========================================================
# Problem    : Remove All Adjacent Duplicates In String
# URL        : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Stack
#
# Acceptance : 73.5%
# Likes      : 7138  |  Dislikes: 276
#
# Language   : python
# Runtime    : 35  (beats 85.16529999999997%)
# Memory     : 13300000  (beats 97.43750000000003%)
# Submitted  : 1782808958
# Exported   : 2026-07-01 11:15:45 UTC
#
# Hints: Use a stack to process everything greedily.
# ==========================================================
class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        """
        :type s: str
        :rtype: str
        """
        
