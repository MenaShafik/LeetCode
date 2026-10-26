# ==========================================================
# Problem    : Split the Array
# URL        : https://leetcode.com/problems/split-the-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 61.9%
# Likes      : 184  |  Dislikes: 17
#
# Language   : python
# Runtime    : 2  (beats 57.554%)
# Memory     : 12096000  (beats 97.12230000000001%)
# Submitted  : 1793000899
# Exported   : 2026-10-26 10:37:01 UTC
#
# Hints: It’s impossible if the same number occurs more than twice. So just check the frequency of each value.
# ==========================================================
class Solution(object):
    def isPossibleToSplit(self, nums):
        n = len(nums)
        if n %2 == 0:
            for i in nums:
                if nums.count(i) > 2:
                    return False
            return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
