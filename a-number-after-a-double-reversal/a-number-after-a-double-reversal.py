# ==========================================================
# Problem    : A Number After a Double Reversal
# URL        : https://leetcode.com/problems/a-number-after-a-double-reversal/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 82.1%
# Likes      : 803  |  Dislikes: 49
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12380000  (beats 57.73479999999999%)
# Submitted  : 1777063241
# Exported   : 2026-04-24 22:38:33 UTC
#
# Hints: Other than the number 0 itself, any number that ends with 0 would lose some digits permanently when reversed.
# ==========================================================
class Solution(object):
    def isSameAfterReversals(self, num):
            if num == 0:
                        return True
            return num % 10 != 0
