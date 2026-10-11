# ==========================================================
# Problem    : Minimum Number of Flips to Reverse Binary String
# URL        : https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Two Pointers, String, Bit Manipulation
#
# Acceptance : 75.5%
# Likes      : 42  |  Dislikes: 1
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12312000  (beats 50.0%)
# Submitted  : 1791709323
# Exported   : 2026-10-11 10:42:30 UTC
#
# Hints: Generate the reverse of the binary string and use two pointers from the ends to determine where flips are needed.
# ==========================================================
class Solution(object):
    def minimumFlips(self, n):
        bin_n = bin(n)[2:]
        reversed_bin = bin_n[::-1]
        counter = 0
        for i in range(len(bin_n)):
            if bin_n[i] != reversed_bin[i]:
                counter+=1
        return counter
        """
        :type n: int
        :rtype: int
        """
        
