# ==========================================================
# Problem    : Binary Search
# URL        : https://leetcode.com/problems/binary-search/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Binary Search
#
# Acceptance : 61.3%
# Likes      : 13677  |  Dislikes: 307
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13200000  (beats 96.33879999999999%)
# Submitted  : 1786463011
# Exported   : 2026-08-11 21:07:09 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            middle = (l+r) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle+1
            else:
                r = middle -1
        return -1
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
