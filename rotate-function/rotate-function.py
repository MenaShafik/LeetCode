# ==========================================================
# Problem    : Rotate Function
# URL        : https://leetcode.com/problems/rotate-function/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Math, Dynamic Programming
#
# Acceptance : 54.1%
# Likes      : 1972  |  Dislikes: 290
#
# Language   : python
# Runtime    : 155  (beats 81.11770000000011%)
# Memory     : 19020000  (beats 77.31190000000002%)
# Submitted  : 1778921188
# Exported   : 2026-05-16 09:13:37 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        f = 0
        for i in range(n):
            f += i * nums[i]
        result = f
        
        for i in range(1, n):
            f = f + total_sum - n * nums[n-i]
            result= max(result, f)
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        
