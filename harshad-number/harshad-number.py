# ================================================================
# Problem : Harshad Number
# URL     : https://leetcode.com/problems/harshad-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 83.3%
# Likes           : 223
# Dislikes        : 13
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12320000  (beats 62.79069999999999%)
# Submitted  : 1776458108
#
# --- Hints ---
# Use a while loop and divide <code>x</code> by <code>10</code> to find the sum of the digits of <code>x</code>.
# ================================================================

class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        sum_digit = sum(int(d) for d in str(x))
        if x % sum_digit == 0:
            return sum_digit
        else:
            return -1
        """
        :type x: int
        :rtype: int
        """
        
