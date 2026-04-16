# ================================================================
# Problem : Sqrt(x)
# URL     : https://leetcode.com/problems/sqrtx/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Binary Search
#
# --- Community Stats ---
# Acceptance Rate : 41.7%
# Likes           : 9713
# Dislikes        : 4641
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12384000  (beats 62.1272%)
# Submitted  : 1769111920
#
# --- Hints ---
# Try exploring all integers. (Credits: @annujoshi)
# Use the sorted property of integers to reduced the search space. (Credits: @annujoshi)
# ================================================================

class Solution(object):
    def mySqrt(self, x):
        self.x = x
        return int(x**0.5)

        """
        :type x: int
        :rtype: int
        """
        
