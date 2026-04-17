# ================================================================
# Problem : Smallest Even Multiple
# URL     : https://leetcode.com/problems/smallest-even-multiple/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Number Theory
#
# --- Community Stats ---
# Acceptance Rate : 88.3%
# Likes           : 1077
# Dislikes        : 127
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12236000  (beats 91.716%)
# Submitted  : 1775080472
#
# --- Hints ---
# A guaranteed way to find a multiple of 2 and n is to multiply them together. When is this the answer, and when is there a smaller answer?
# There is a smaller answer when n is even.
# ================================================================

class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 != 0:
            return n*2
        else:
            return n
        """
        :type n: int
        :rtype: int
        """
        
