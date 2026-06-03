# ==========================================================
# Problem    : Intersection of Two Arrays II
# URL        : https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Two Pointers, Binary Search, Sorting
#
# Acceptance : 59.9%
# Likes      : 8224  |  Dislikes: 1010
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12640000  (beats 4.5323999999999955%)
# Submitted  : 1780479372
# Exported   : 2026-06-03 09:37:56 UTC
#
# Hints: N/A
# ==========================================================
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        result = []
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
        return result

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
