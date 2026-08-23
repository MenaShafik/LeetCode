# ==========================================================
# Problem    : Largest Odd Number in String
# URL        : https://leetcode.com/problems/largest-odd-number-in-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Greedy
#
# Acceptance : 68.0%
# Likes      : 2658  |  Dislikes: 150
#
# Language   : python
# Runtime    : 31  (beats 81.61189999999996%)
# Memory     : 17168000  (beats 19.34019999999995%)
# Submitted  : 1787475118
# Exported   : 2026-08-23 21:47:15 UTC
#
# Hints: In what order should you iterate through the digits?
#   If an odd number exists, where must the number start from?
# ==========================================================
class Solution(object):
    def largestOddNumber(self, num):
        
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""

        """
        :type num: str
        :rtype: str
        """
        
