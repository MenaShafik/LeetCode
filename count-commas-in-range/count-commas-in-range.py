# ==========================================================
# Problem    : Count Commas in Range
# URL        : https://leetcode.com/problems/count-commas-in-range/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 75.8%
# Likes      : 178  |  Dislikes: 16
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12568000  (beats 17.475800000000007%)
# Submitted  : 1788856833
# Exported   : 2026-09-08 11:10:42 UTC
#
# Hints: Numbers in the range <code>[1000, 100000]</code> have one comma.
# ==========================================================
class Solution(object):
    def countCommas(self, n):
        if n<=999:
            return 0

        if n>999 and n<=99999:
            return n-1000+1

        if n>9999 and n<=100000:
            return n-1000+1
        """
        :type n: int
        :rtype: int
        """
        
