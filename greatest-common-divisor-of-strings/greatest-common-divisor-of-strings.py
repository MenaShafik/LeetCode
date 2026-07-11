# ==========================================================
# Problem    : Greatest Common Divisor of Strings
# URL        : https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String
#
# Acceptance : 54.0%
# Likes      : 6072  |  Dislikes: 1668
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12328000  (beats 63.501400000000004%)
# Submitted  : 1783760994
# Exported   : 2026-07-11 09:14:50 UTC
#
# Hints: The greatest common divisor must be a prefix of each string, so we can try all prefixes.
# ==========================================================
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        length_gcd = gcd(len(str1), len(str2))
        return str1[:length_gcd]

        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
