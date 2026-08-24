# ==========================================================
# Problem    : Count Odd Numbers in an Interval Range
# URL        : https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 54.8%
# Likes      : 3150  |  Dislikes: 182
#
# Language   : python
# Runtime    : 3  (beats 99.7006%)
# Memory     : 12448000  (beats 14.970199999999984%)
# Submitted  : 1787562865
# Exported   : 2026-08-24 16:10:51 UTC
#
# Hints: If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same.
#   If the range (high - low + 1) is odd, the solution will depend on the parity of high and low.
# ==========================================================
class Solution(object):
    def countOdds(self, low, high):
        return (high+1)//2 - low //2
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
