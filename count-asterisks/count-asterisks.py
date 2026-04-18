# ==========================================================
# Problem    : Count Asterisks
# URL        : https://leetcode.com/problems/count-asterisks/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String
#
# Acceptance : 83.3%
# Likes      : 683  |  Dislikes: 118
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12380000  (beats 70.1031%)
# Submitted  : 1776540658
# Exported   : 2026-04-18 19:41:35 UTC
#
# Hints: Iterate through each character, while maintaining whether we are currently between a pair of ‘|’ or not.
#   If we are not in between a pair of ‘|’ and there is a ‘*’, increment the answer by 1.
# ==========================================================
class Solution(object):
    def countAsterisks(self, s):
        astr=0
        flag = False
        for i in s:
            if i == '|':
                flag = not flag
            elif i == '*' and not flag:
                astr+=1
        return astr
        """
        :type s: str
        :rtype: int
        """
