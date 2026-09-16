# ==========================================================
# Problem    : Maximum Odd Binary Number
# URL        : https://leetcode.com/problems/maximum-odd-binary-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, String, Greedy
#
# Acceptance : 82.8%
# Likes      : 851  |  Dislikes: 34
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12296000  (beats 90.2326%)
# Submitted  : 1789548688
# Exported   : 2026-09-16 09:00:41 UTC
#
# Hints: The binary representation of an odd number contains <code>'1'</code> in the least significant place.
# ==========================================================
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        ones = s.count("1")
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1"
        """
        :type s: str
        :rtype: str
        """
        
