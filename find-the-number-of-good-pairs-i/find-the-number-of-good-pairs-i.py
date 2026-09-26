# ==========================================================
# Problem    : Find the Number of Good Pairs I
# URL        : https://leetcode.com/problems/find-the-number-of-good-pairs-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 86.2%
# Likes      : 179  |  Dislikes: 17
#
# Language   : python
# Runtime    : 3  (beats 95.65220000000001%)
# Memory     : 12348000  (beats 57.39129999999999%)
# Submitted  : 1790411912
# Exported   : 2026-09-26 08:43:41 UTC
#
# Hints: The constraints are small. Check all pairs.
# ==========================================================
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        counter = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) ==0:
                    counter +=1
        return counter 
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
