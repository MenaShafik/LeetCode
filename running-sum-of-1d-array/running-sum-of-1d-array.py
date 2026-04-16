# ================================================================
# Problem : Running Sum of 1d Array
# URL     : https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Prefix Sum
#
# --- Community Stats ---
# Acceptance Rate : 86.9%
# Likes           : 8804
# Dislikes        : 371
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12368000  (beats 97.5273%)
# Submitted  : 1775591905
#
# --- Hints ---
# Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.
# ================================================================

class Solution(object):
    def runningSum(self, nums):
        result = []
        sum = 0
        for i in nums:
            sum+= i
            result.append(sum)
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
