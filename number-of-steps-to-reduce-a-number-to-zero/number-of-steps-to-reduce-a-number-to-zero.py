# ==========================================================
# Problem    : Number of Steps to Reduce a Number to Zero
# URL        : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Bit Manipulation
#
# Acceptance : 85.8%
# Likes      : 4285  |  Dislikes: 181
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12420000  (beats 23.836400000000005%)
# Submitted  : 1776716237
# Exported   : 2026-04-20 21:17:42 UTC
#
# Hints: Simulate the process to get the final answer.
# ==========================================================
class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1

            steps += 1
        return steps
        """
        :type num: int
        :rtype: int
        """
        
