# ==========================================================
# Problem    : Self Dividing Numbers
# URL        : https://leetcode.com/problems/self-dividing-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 80.8%
# Likes      : 1949  |  Dislikes: 387
#
# Language   : python
# Runtime    : 3  (beats 99.21759999999999%)
# Memory     : 12652000  (beats 16.036599999999993%)
# Submitted  : 1779707698
# Exported   : 2026-05-25 11:29:04 UTC
#
# Hints: For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), then checking that each digit is nonzero and divides the original number.
# ==========================================================
class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        for num in range(left, right + 1):
            temp = num
            valid = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    valid = False
                    break
                temp //= 10
            if valid:
                result.append(num)
        return result

        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
