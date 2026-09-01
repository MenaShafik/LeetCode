# ==========================================================
# Problem    : Average Value of Even Numbers That Are Divisible by Three
# URL        : https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 63.7%
# Likes      : 383  |  Dislikes: 42
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12352000  (beats 91.4474%)
# Submitted  : 1788253827
# Exported   : 2026-09-01 09:16:02 UTC
#
# Hints: What is the property of a number if it is divisible by both 2 and 3 at the same time?
#   It is equivalent to finding all the numbers that are divisible by 6.
# ==========================================================
class Solution(object):
    def averageValue(self, nums):
        sumValue = 0
        count = 0

        for num in nums:
            if num % 6 == 0:
                sumValue += num
                count += 1

        if count == 0:
            return 0

        return sumValue // count
        """
        :type nums: List[int]
        :rtype: int
        """
        
