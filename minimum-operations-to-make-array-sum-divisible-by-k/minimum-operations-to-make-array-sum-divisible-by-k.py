# ==========================================================
# Problem    : Minimum Operations to Make Array Sum Divisible by K
# URL        : https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 92.3%
# Likes      : 342  |  Dislikes: 38
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12636000  (beats 11.7453%)
# Submitted  : 1778245122
# Exported   : 2026-05-08 13:05:20 UTC
#
# Hints: <code> sum(nums) % k </code>
# ==========================================================
class Solution(object):
    def minOperations(self, nums, k):
       
        return sum(nums)%k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
