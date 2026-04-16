# ================================================================
# Problem : Power of Three
# URL     : https://leetcode.com/problems/power-of-three/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Recursion
#
# --- Community Stats ---
# Acceptance Rate : 51.0%
# Likes           : 3722
# Dislikes        : 317
#
# --- My Submission ---
# Language   : python
# Runtime    : 4  (beats 92.9465%)
# Memory     : 12448000  (beats 25.955499999999994%)
# Submitted  : 1773013681
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
