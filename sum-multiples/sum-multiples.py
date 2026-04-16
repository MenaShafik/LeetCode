# ================================================================
# Problem : Sum Multiples
# URL     : https://leetcode.com/problems/sum-multiples/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# --- Community Stats ---
# Acceptance Rate : 85.9%
# Likes           : 598
# Dislikes        : 44
#
# --- My Submission ---
# Language   : python
# Runtime    : 12  (beats 98.2624%)
# Memory     : 12484000  (beats 30.308899999999994%)
# Submitted  : 1775770138
#
# --- Hints ---
# Iterate through the range 1 to n and count numbers divisible by either 3, 5, or 7.
# ================================================================

class Solution(object):
    def sumOfMultiples(self, n):
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total

        """
        :type n: int
        :rtype: int
        """
        
