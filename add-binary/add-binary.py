# ==========================================================
# Problem    : Add Binary
# URL        : https://leetcode.com/problems/add-binary/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Bit Manipulation, Simulation
#
# Acceptance : 58.5%
# Likes      : 10885  |  Dislikes: 1121
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12212000  (beats 93.0669%)
# Submitted  : 1786522947
# Exported   : 2026-08-12 13:56:26 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def addBinary(self, a, b):
        
        result = bin(int(a, 2) + int(b, 2))[2:]
        return result

        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
