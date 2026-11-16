# ==========================================================
# Problem    : Maximum Number of Operations With the Same Score I
# URL        : https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# Acceptance : 53.2%
# Likes      : 97  |  Dislikes: 29
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12068000  (beats 96.1538%)
# Submitted  : 1794818630
# Exported   : 2026-11-16 11:39:47 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def maxOperations(self, nums):
        operations = 0
        s = nums[0]+nums[1]

        for i in range(0,len(nums)-1,2):
            if s == nums[i]+nums[i+1]:
                operations+=1
            else:
                break
        return operations
        """
        :type nums: List[int]
        :rtype: int
        """
        
