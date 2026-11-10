# ==========================================================
# Problem    : Check if Array is Good
# URL        : https://leetcode.com/problems/check-if-array-is-good/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 57.3%
# Likes      : 490  |  Dislikes: 73
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12040000  (beats 97.9943%)
# Submitted  : 1794300879
# Exported   : 2026-11-10 09:29:20 UTC
#
# Hints: Find the maximum element of the array.
# ==========================================================
class Solution(object):
    def isGood(self, nums):
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i] != i+1:     
                return False
        if nums[n-1] == n-1:
            return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
