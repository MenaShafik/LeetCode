# ==========================================================
# Problem    : Form Smallest Number From Two Digit Arrays
# URL        : https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Enumeration
#
# Acceptance : 55.4%
# Likes      : 331  |  Dislikes: 29
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12416000  (beats 22.2222%)
# Submitted  : 1789749431
# Exported   : 2026-09-18 21:35:04 UTC
#
# Hints: How many digits will the resulting number have at most?
#   The resulting number will have either one or two digits. Try to find when each case is possible.
# ==========================================================
class Solution(object):
    def minNumber(self, nums1, nums2):
        common = set(nums1) & set(nums2)
        if common:
            return  min(common)
        if min(nums1) > min(nums2):
            return min(nums2) * 10 +min(nums1)
        return min(nums1) * 10 +min(nums2) 
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
