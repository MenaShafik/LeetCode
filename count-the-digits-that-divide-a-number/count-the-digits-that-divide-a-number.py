# ================================================================
# Problem : Count the Digits That Divide a Number
# URL     : https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 85.9%
# Likes           : 686
# Dislikes        : 44
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12320000  (beats 64.294%)
# Submitted  : 1775853183
#
# --- Hints ---
# Use mod by 10 to retrieve the least significant digit of the number
# Divide the number by 10, then round it down so that the second least significant digit becomes the least significant digit of the number
# Use your language’s mod operator to see if a number is a divisor of another.
# ================================================================

class Solution(object):
    def countDigits(self, num):
        st = str(num)
        val = 0
        for i in st:
            if num % int(i)==0:
                val+=1
        return val
        """
        :type num: int
        :rtype: int
        """
        
