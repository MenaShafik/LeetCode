# ==========================================================
# Problem    : Sum of All Odd Length Subarrays
# URL        : https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Prefix Sum
#
# Acceptance : 84.1%
# Likes      : 3934  |  Dislikes: 331
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12284000  (beats 93.75%)
# Submitted  : 1786041128
# Exported   : 2026-08-06 18:38:07 UTC
#
# Hints: You can brute force – try every (i,j) pair, and if the length is odd, go through and add the sum to the answer.
# ==========================================================
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        sum_arr = 0
        for i in range(n):
            left_count = i + 1
            right_count = n - i
            total_subarrays = left_count * right_count
            odd_subarrays = (total_subarrays + 1) // 2
                
            sum_arr+= arr[i] * odd_subarrays
        return sum_arr

        """
        :type arr: List[int]
        :rtype: int
        """
        
