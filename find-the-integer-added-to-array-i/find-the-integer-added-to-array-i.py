# ==========================================================
# Problem    : Find the Integer Added to Array I
# URL        : https://leetcode.com/problems/find-the-integer-added-to-array-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 82.9%
# Likes      : 173  |  Dislikes: 12
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12208000  (beats 97.7778%)
# Submitted  : 1776631986
# Exported   : 2026-04-19 21:26:59 UTC
#
# Hints: Notice that, after sorting both arrays, there should be a one-to-one correspondence between every element.
#   Thus <code>x = min(nums2) - min(nums1)</code>.
# ==========================================================
class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        return nums2[0]-nums1[0]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
