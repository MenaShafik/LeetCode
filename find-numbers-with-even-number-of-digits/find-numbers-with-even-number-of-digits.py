# ==========================================================
# Problem    : Find Numbers with Even Number of Digits
# URL        : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 79.7%
# Likes      : 2969  |  Dislikes: 150
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12344000  (beats 70.05189999999999%)
# Submitted  : 1777925461
# Exported   : 2026-05-04 20:11:59 UTC
#
# Hints: How to compute the number of digits of a number ?
#   Divide the number by 10 again and again to get the number of digits.
# ==========================================================
class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        
