# ==========================================================
# Problem    : Find Greatest Common Divisor of Array
# URL        : https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Number Theory
#
# Acceptance : 82.0%
# Likes      : 1391  |  Dislikes: 56
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12264000  (beats 99.6386%)
# Submitted  : 1784363095
# Exported   : 2026-07-18 08:50:30 UTC
#
# Hints: Find the minimum and maximum in one iteration. Let them be mn and mx.
#   Try all the numbers in the range [1, mn] and check the largest number which divides both of them.
# ==========================================================
class Solution(object):
    def findGCD(self, nums):
        mini = min(nums)
        maxi = max(nums)
        while mini != 0:
            maxi, mini = mini, maxi % mini
        return maxi
        """
        :type nums: List[int]
        :rtype: int
        """
        
