# ==========================================================
# Problem    : Compute Alternating Sum
# URL        : https://leetcode.com/problems/compute-alternating-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# Acceptance : 90.0%
# Likes      : 67  |  Dislikes: 2
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12356000  (beats 52.0548%)
# Submitted  : 1778153003
# Exported   : 2026-05-07 11:25:23 UTC
#
# Hints: Simulate as described
# ==========================================================
class Solution(object):
    def alternatingSum(self, nums):
        return sum(num if i % 2 == 0 else -num for i, num in enumerate(nums))
        
