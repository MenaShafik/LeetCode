# ==========================================================
# Problem    : Number Complement
# URL        : https://leetcode.com/problems/number-complement/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Bit Manipulation
#
# Acceptance : 70.5%
# Likes      : 3243  |  Dislikes: 146
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12448000  (beats 14.634199999999993%)
# Submitted  : 1781602859
# Exported   : 2026-06-16 09:55:17 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findComplement(self, num):
        binary = bin(num)[2:]  # Convert to binary and remove '0b' prefix
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        return int(complement, 2)  # Convert back to decimal
        """
        :type num: int
        :rtype: int
        """
        
