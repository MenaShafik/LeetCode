# ==========================================================
# Problem    : Maximum 69 Number
# URL        : https://leetcode.com/problems/maximum-69-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Greedy
#
# Acceptance : 84.6%
# Likes      : 3319  |  Dislikes: 240
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12480000  (beats 20.6434%)
# Submitted  : 1776976494
# Exported   : 2026-04-23 20:41:14 UTC
#
# Hints: Convert the number in an array of its digits.
#   Brute force on every digit to get the maximum number.
# ==========================================================
class Solution(object):
    def maximum69Number (self, num):
        return int(str(num).replace('6', '9', 1))
        """
        :type num: int
        :rtype: int
        """
        
