# ==========================================================
# Problem    : Minimum Operations to Equalize Array
# URL        : https://leetcode.com/problems/minimum-operations-to-equalize-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Bit Manipulation, Brainteaser
#
# Acceptance : 60.9%
# Likes      : 64  |  Dislikes: 14
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12016000  (beats 100.0%)
# Submitted  : 1793779442
# Exported   : 2026-11-04 11:08:16 UTC
#
# Hints: If all elements of <code>nums</code> are already equal, how many operations are needed?
#   The answer is either <code>0</code> or <code>1</code>.
#   The answer is <code>0</code> if all values in the array are initially equal, and <code>1</code> otherwise, since you can apply the AND operation on the whole array in one step.
# ==========================================================
class Solution(object):
    def minOperations(self, nums):
        if len(set(nums)) == 1:
            return 0
        return 1
        """
        :type nums: List[int]
        :rtype: int
        """
        
