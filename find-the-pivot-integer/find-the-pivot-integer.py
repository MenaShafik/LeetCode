# ==========================================================
# Problem    : Find the Pivot Integer
# URL        : https://leetcode.com/problems/find-the-pivot-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Prefix Sum
#
# Acceptance : 83.8%
# Likes      : 1460  |  Dislikes: 60
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12424000  (beats 24.039699999999982%)
# Submitted  : 1779529541
# Exported   : 2026-05-23 09:51:41 UTC
#
# Hints: Can you use brute force to check every number from 1 to n if any of them is the pivot integer?
#   If you know the sum of [1: pivot], how can you efficiently calculate the sum of the other parts?
# ==========================================================
class Solution(object):
    def pivotInteger(self, n):
        total_sum = n * (n+1) //2
        left_num =0
        for i in range(1,n+1):
            left_num+=i
            if left_num == total_sum - left_num + i:
                return i
        return -1



        
        """
        :type n: int
        :rtype: int
        """
        
