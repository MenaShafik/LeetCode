# ==========================================================
# Problem    : Base 7
# URL        : https://leetcode.com/problems/base-7/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 54.7%
# Likes      : 895  |  Dislikes: 240
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12264000  (beats 88.9435%)
# Submitted  : 1782034995
# Exported   : 2026-06-21 09:45:18 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        stack = []
        while num:
            stack.append(str(num%7))
            num//=7
        if negative:
            stack.append("-")
        return ''.join(reversed(stack))
        """
        :type num: int
        :rtype: str
        """
        
