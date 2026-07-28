# ==========================================================
# Problem    : Minimum Sum of Four Digit Number After Splitting Digits
# URL        : https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Greedy, Sorting
#
# Acceptance : 86.3%
# Likes      : 1525  |  Dislikes: 148
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12460000  (beats 16.230300000000007%)
# Submitted  : 1785228978
# Exported   : 2026-07-28 09:10:47 UTC
#
# Hints: Notice that the most optimal way to obtain the minimum possible sum using 4 digits is by summing up two 2-digit numbers.
#   We can use the two smallest digits out of the four as the digits found in the tens place respectively.
#   Similarly, we use the final 2 larger digits as the digits found in the ones place.
# ==========================================================
class Solution(object):
    def minimumSum(self, num):
        digits = sorted(str(num))

        num1 = int(digits[0] + digits[2])
        num2 = int(digits[1] + digits[3])

        return num1 + num2

        """
        :type num: int
        :rtype: int
        """
        
