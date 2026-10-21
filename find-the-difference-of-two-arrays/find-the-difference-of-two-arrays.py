# ==========================================================
# Problem    : Find the Difference of Two Arrays
# URL        : https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 81.7%
# Likes      : 2680  |  Dislikes: 129
#
# Language   : python
# Runtime    : 6  (beats 75.6851%)
# Memory     : 12508000  (beats 92.26989999999999%)
# Submitted  : 1792566298
# Exported   : 2026-10-21 09:11:26 UTC
#
# Hints: For each integer in nums1, check if it exists in nums2.
#   Do the same for each integer in nums2.
# ==========================================================
class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        diff_1 = list(nums1_set - nums2_set)
        diff_2 = list(nums2_set - nums1_set)
        return [diff_1 , diff_2]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
