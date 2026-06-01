# ==========================================================
# Problem    : Digit Frequency Score
# URL        : https://leetcode.com/problems/digit-frequency-score/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : N/A
#
# Acceptance : 91.2%
# Likes      : 17  |  Dislikes: 0
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12460000  (beats 100.0%)
# Submitted  : 1780303772
# Exported   : 2026-06-01 08:56:19 UTC
#
# Hints: The answer is the sum of the digits.
# ==========================================================
class Solution(object):
    def digitFrequencyScore(self, n):
        k = str(n)
        total = 0
        for digit in set(k):
            total += int(digit) * k.count(digit)
        return total
        """
        :type n: int
        :rtype: int
        """
        
