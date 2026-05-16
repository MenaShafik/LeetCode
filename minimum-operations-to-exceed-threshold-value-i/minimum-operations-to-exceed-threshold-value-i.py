# ==========================================================
# Problem    : Minimum Operations to Exceed Threshold Value I
# URL        : https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 86.8%
# Likes      : 175  |  Dislikes: 17
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12524000  (beats 0.3649000000000129%)
# Submitted  : 1778922718
# Exported   : 2026-05-16 09:13:35 UTC
#
# Hints: Iterate over <code>nums</code> and count the number of elements less than <code>k</code>.
# ==========================================================
class Solution(object):
    def minOperations(self, nums, k):
        count = 0
        for x in nums:
            if x < k:
                count += 1
        return count

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
