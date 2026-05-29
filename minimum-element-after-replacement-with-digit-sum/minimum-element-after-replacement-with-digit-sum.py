# ==========================================================
# Problem    : Minimum Element After Replacement With Digit Sum
# URL        : https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math
#
# Acceptance : 88.8%
# Likes      : 206  |  Dislikes: 5
#
# Language   : python
# Runtime    : 3  (beats 95.4129%)
# Memory     : 12512000  (beats 2.7522000000000055%)
# Submitted  : 1780058478
# Exported   : 2026-05-29 12:46:54 UTC
#
# Hints: Convert to string and calculate the sum for each element.
# ==========================================================
class Solution(object):
    def minElement(self, nums):
        minimum=float("inf")
        for num in nums:
            digitsum=0
            while num>0:
                digitsum+=num%10
                num//=10
            minimum=min(minimum,digitsum)
        return minimum

        """
        :type nums: List[int]
        :rtype: int
        """
        
