# ==========================================================
# Problem    : Transform Array by Parity
# URL        : https://leetcode.com/problems/transform-array-by-parity/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting, Counting
#
# Acceptance : 89.8%
# Likes      : 108  |  Dislikes: 8
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12288000  (beats 91.2791%)
# Submitted  : 1778581958
# Exported   : 2026-05-12 10:34:07 UTC
#
# Hints: Let <code>x</code> be the number of even numbers, and <code>y</code> be the number of odd numbers. Output <code>0</code> <code>x</code> times, followed by <code>1</code> <code>y</code> times.
# ==========================================================
class Solution(object):
    def transformArray(self, nums):
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        return sorted(nums)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
