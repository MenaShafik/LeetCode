# ==========================================================
# Problem    : Minimum Bit Flips to Convert Number
# URL        : https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Bit Manipulation
#
# Acceptance : 88.0%
# Likes      : 1668  |  Dislikes: 40
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12232000  (beats 89.3939%)
# Submitted  : 1791546359
# Exported   : 2026-10-10 11:52:14 UTC
#
# Hints: If the value of a bit in start and goal differ, then we need to flip that bit.
#   Consider using the XOR operation to determine which bits need a bit flip.
# ==========================================================
class Solution(object):
    def minBitFlips(self, start, goal):
        return bin(start ^ goal).count("1")
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        
