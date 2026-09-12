# ==========================================================
# Problem    : Find the Duplicate Number
# URL        : https://leetcode.com/problems/find-the-duplicate-number/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Two Pointers, Binary Search, Bit Manipulation, Pigeonhole Principle, Floyd's Cycle Finding Algorithm
#
# Acceptance : 64.9%
# Likes      : 25870  |  Dislikes: 5942
#
# Language   : python
# Runtime    : 27  (beats 87.5592%)
# Memory     : 27252000  (beats 10.315499999999982%)
# Submitted  : 1789199830
# Exported   : 2026-09-12 21:37:27 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)


        """
        :type nums: List[int]
        :rtype: int
        """
        
