# ==========================================================
# Problem    : Minimum Common Value
# URL        : https://leetcode.com/problems/minimum-common-value/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Two Pointers, Binary Search
#
# Acceptance : 60.8%
# Likes      : 1399  |  Dislikes: 44
#
# Language   : python
# Runtime    : 11  (beats 85.16960000000002%)
# Memory     : 24300000  (beats 58.0509%)
# Submitted  : 1779219969
# Exported   : 2026-05-20 07:40:24 UTC
#
# Hints: Try to use a set.
#   Otherwise, try to use a two-pointer approach.
# ==========================================================
class Solution(object):
    def getCommon(self, nums1, nums2):
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
