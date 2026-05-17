# ==========================================================
# Problem    : Final Array State After K Multiplication Operations I
# URL        : https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Heap (Priority Queue), Simulation
#
# Acceptance : 86.9%
# Likes      : 555  |  Dislikes: 13
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12200000  (beats 99.3939%)
# Submitted  : 1779009182
# Exported   : 2026-05-17 09:15:11 UTC
#
# Hints: Maintain sorted pairs <code>(nums[index], index)</code> in a priority queue.
#   Simulate the operation <code>k</code> times.
# ==========================================================
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier 
        return nums
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        
