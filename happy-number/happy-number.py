# ================================================================
# Problem : Happy Number
# URL     : https://leetcode.com/problems/happy-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, Math, Two Pointers
#
# --- Community Stats ---
# Acceptance Rate : 59.5%
# Likes           : 11954
# Dislikes        : 1645
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12336000  (beats 60.03750000000001%)
# Submitted  : 1769112821
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            s = 0
            while n > 0:
                digit = n % 10
                s += digit * digit
                n //= 10

            n = s

        return True

        """
        :type n: int
        :rtype: bool
        """
        
