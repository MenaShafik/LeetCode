# ==========================================================
# Problem    : Shuffle the Array
# URL        : https://leetcode.com/problems/shuffle-the-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 88.8%
# Likes      : 6441  |  Dislikes: 359
#
# Language   : python
# Runtime    : 38  (beats 71.46850000000002%)
# Memory     : 12476000  (beats 81.9642%)
# Submitted  : 1778669562
# Exported   : 2026-05-14 09:59:05 UTC
#
# Hints: Use two pointers to create the new array of 2n elements. The first starting at the beginning and the other starting at (n+1)th position. Alternate between them and create the new array.
# ==========================================================
class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n,len(nums)):
            result.append(nums[i-n])
            result.append(nums[i])
        return result

        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
