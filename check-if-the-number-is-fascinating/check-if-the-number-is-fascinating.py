# ==========================================================
# Problem    : Check if The Number is Fascinating
# URL        : https://leetcode.com/problems/check-if-the-number-is-fascinating/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, Math
#
# Acceptance : 53.0%
# Likes      : 267  |  Dislikes: 15
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12460000  (beats 15.662599999999976%)
# Submitted  : 1788941440
# Exported   : 2026-09-09 12:46:54 UTC
#
# Hints: Consider changing the number to the way it is described in the statement.
#   Check if the resulting number contains all the digits from 1 to 9 exactly once.
# ==========================================================
class Solution(object):
    def isFascinating(self, n):
        numbers = "123456789"
        numbers_chars = str(n)+str(2*n)+ str(3*n)
        return len(numbers_chars) == 9 and set(numbers_chars) == set(numbers)
        """
        :type n: int
        :rtype: bool
        """
        
