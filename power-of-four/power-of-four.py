# ================================================================
# Problem : Power of Four
# URL     : https://leetcode.com/problems/power-of-four/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Bit Manipulation, Recursion
#
# --- Community Stats ---
# Acceptance Rate : 51.9%
# Likes           : 4489
# Dislikes        : 423
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12380000  (beats 60.82530000000001%)
# Submitted  : 1772393298
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def isPowerOfFour(self, n):

        if n <= 0:
            return False
        return math.log(n, 4).is_integer()
        """
        :type n: int
        :rtype: bool
        """
        
