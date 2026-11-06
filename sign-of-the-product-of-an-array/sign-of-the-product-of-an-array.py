# ==========================================================
# Problem    : Sign of the Product of an Array
# URL        : https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 64.6%
# Likes      : 2327  |  Dislikes: 234
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12364000  (beats 74.063%)
# Submitted  : 1793986250
# Exported   : 2026-11-06 17:44:54 UTC
#
# Hints: If there is a 0 in the array the answer is 0
#   To avoid overflow make all the negative numbers -1 and all positive numbers 1 and calculate the prod
# ==========================================================
class Solution(object):
    def arraySign(self, nums):
        negative = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                negative+=1
        if negative % 2 == 0:
            return 1
        else:
            return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        
