# ==========================================================
# Problem    : Hamming Distance
# URL        : https://leetcode.com/problems/hamming-distance/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Bit Manipulation
#
# Acceptance : 77.1%
# Likes      : 4059  |  Dislikes: 231
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12292000  (beats 90.4274%)
# Submitted  : 1790948177
# Exported   : 2026-10-03 15:55:23 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y).count("1")
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
