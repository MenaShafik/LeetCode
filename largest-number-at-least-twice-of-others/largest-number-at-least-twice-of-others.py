# ==========================================================
# Problem    : Largest Number At Least Twice of Others
# URL        : https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting
#
# Acceptance : 52.8%
# Likes      : 1391  |  Dislikes: 961
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12360000  (beats 55.81400000000001%)
# Submitted  : 1784193200
# Exported   : 2026-07-16 09:28:15 UTC
#
# Hints: Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`.

Scan through the array again.  If we find some `x != m` with `m < 2*x`, we should return `-1`.

Otherwise, we should return `maxIndex`.
# ==========================================================
class Solution(object):
    def dominantIndex(self, nums):
        max_number = max(nums)
        index = nums.index(max_number)
        for i in nums:
            if i != max_number and max_number < 2 * i:
                return -1
        return index
        """
        :type nums: List[int]
        :rtype: int
        """
        
