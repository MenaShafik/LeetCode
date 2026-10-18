# ==========================================================
# Problem    : Count Integers With Even Digit Sum
# URL        : https://leetcode.com/problems/count-integers-with-even-digit-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Simulation
#
# Acceptance : 71.1%
# Likes      : 740  |  Dislikes: 44
#
# Language   : python
# Runtime    : 26  (beats 29.3812%)
# Memory     : 12156000  (beats 97.4227%)
# Submitted  : 1792305968
# Exported   : 2026-10-18 12:31:04 UTC
#
# Hints: Iterate through all integers from 1 to num.
#   For any integer, extract the individual digits to compute their sum and check if it is even.
# ==========================================================
class Solution(object):
    def countEven(self, num):
        counter = 0
        for i in range(1,num+1):
            digit_sum = sum(int(digit) for digit in str(i))
            if digit_sum %2 ==0:
                counter +=1
        return counter
        """
        :type num: int
        :rtype: int
        """
        
