# ==========================================================
# Problem    : Sort Integers by The Number of 1 Bits
# URL        : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Bit Manipulation, Sorting, Counting
#
# Acceptance : 82.4%
# Likes      : 2883  |  Dislikes: 139
#
# Language   : python
# Runtime    : 3  (beats 96.08800000000001%)
# Memory     : 12480000  (beats 79.9511%)
# Submitted  : 1787733731
# Exported   : 2026-08-26 18:21:02 UTC
#
# Hints: Simulate the problem. Count the number of 1's in the binary representation of each integer.
#   Sort by the number of 1's ascending and by the value in case of tie.
# ==========================================================
class Solution(object):
    def sortByBits(self, arr):

        return sorted(arr,key=lambda x: (bin(x).count("1"), x))
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
