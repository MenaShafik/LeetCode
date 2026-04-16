# ================================================================
# Problem : Transformed Array
# URL     : https://leetcode.com/problems/transformed-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# --- Community Stats ---
# Acceptance Rate : 70.5%
# Likes           : 453
# Dislikes        : 47
#
# --- My Submission ---
# Language   : python
# Runtime    : 31  (beats 93.75%)
# Memory     : 12392000  (beats 75.41669999999999%)
# Submitted  : 1770304060
#
# --- Hints ---
# Simulate the operations as described in the statement
# ================================================================

class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            result.append(0)
        for i in range(n):
            a = nums[i]
            result[i] = nums[(i+a)%n]
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
