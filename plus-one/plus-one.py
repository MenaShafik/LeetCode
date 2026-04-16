# ================================================================
# Problem : Plus One
# URL     : https://leetcode.com/problems/plus-one/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# --- Community Stats ---
# Acceptance Rate : 49.8%
# Likes           : 11864
# Dislikes        : 5611
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12416000  (beats 26.269299999999994%)
# Submitted  : 1773261427
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0 
        return [1] + digits
