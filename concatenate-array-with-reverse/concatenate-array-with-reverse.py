# ==========================================================
# Problem    : Concatenate Array With Reverse
# URL        : https://leetcode.com/problems/concatenate-array-with-reverse/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : N/A
#
# Acceptance : 91.6%
# Likes      : 10  |  Dislikes: 1
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12288000  (beats 99.0347%)
# Submitted  : 1778403119
# Exported   : 2026-05-10 09:01:22 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def concatWithReverse(self, nums):
        ans = nums
        for i in reversed(nums):
            ans.append(i)
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
