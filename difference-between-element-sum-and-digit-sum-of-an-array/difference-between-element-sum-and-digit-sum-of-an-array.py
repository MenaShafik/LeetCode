# ================================================================
# Problem : Difference Between Element Sum and Digit Sum of an Array
# URL     : https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# --- Community Stats ---
# Acceptance Rate : 85.3%
# Likes           : 819
# Dislikes        : 32
#
# --- My Submission ---
# Language   : python
# Runtime    : 11  (beats 94.5946%)
# Memory     : 12536000  (beats 68.4685%)
# Submitted  : 1776117739
#
# --- Hints ---
# Use a simple for loop to iterate each number.
# How you can get the digit for each number?
# ================================================================

class Solution(object):
    def differenceOfSum(self, nums):

        element = sum(nums)
        digit = 0
        for i in nums:
            while i>9:
                digit+=i%10
                i//=10
            else:digit+=i
        
        return abs(element - digit)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
