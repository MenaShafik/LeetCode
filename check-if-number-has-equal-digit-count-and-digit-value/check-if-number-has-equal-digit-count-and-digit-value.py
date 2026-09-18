# ==========================================================
# Problem    : Check if Number Has Equal Digit Count and Digit Value
# URL        : https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String, Counting
#
# Acceptance : 73.3%
# Likes      : 691  |  Dislikes: 101
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12372000  (beats 52.38099999999999%)
# Submitted  : 1789633493
# Exported   : 2026-09-18 21:35:08 UTC
#
# Hints: Count the frequency of each digit in num.
# ==========================================================
class Solution(object):
    def digitCount(self, num):
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                return False
        return True
        """
        :type num: str
        :rtype: bool
        """
        
