# ==========================================================
# Problem    : Perfect Number
# URL        : https://leetcode.com/problems/perfect-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 48.8%
# Likes      : 1310  |  Dislikes: 1290
#
# Language   : python
# Runtime    : 4  (beats 85.4007%)
# Memory     : 12580000  (beats 31.72329999999998%)
# Submitted  : 1779310559
# Exported   : 2026-05-21 09:16:03 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        divisors_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        return divisors_sum == num

        """
        :type num: int
        :rtype: bool
        """
        
