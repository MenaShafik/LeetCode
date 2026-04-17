# ================================================================
# Problem : Power of Two
# URL     : https://leetcode.com/problems/power-of-two/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Bit Manipulation, Recursion
#
# --- Community Stats ---
# Acceptance Rate : 50.0%
# Likes           : 8068
# Dislikes        : 505
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12316000  (beats 62.72%)
# Submitted  : 1772912515
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True
