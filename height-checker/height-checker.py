# ==========================================================
# Problem    : Height Checker
# URL        : https://leetcode.com/problems/height-checker/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting, Counting Sort
#
# Acceptance : 81.7%
# Likes      : 1801  |  Dislikes: 123
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12324000  (beats 57.18200000000001%)
# Submitted  : 1777494525
# Exported   : 2026-04-29 23:07:31 UTC
#
# Hints: Build the correct order of heights by sorting another array, then compare the two arrays.
# ==========================================================
class Solution(object):
    def heightChecker(self, heights):

        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count

        """
        :type heights: List[int]
        :rtype: int
        """
        
