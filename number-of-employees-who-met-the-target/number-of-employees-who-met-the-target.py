# ================================================================
# Problem : Number of Employees Who Met the Target
# URL     : https://leetcode.com/problems/number-of-employees-who-met-the-target/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# --- Community Stats ---
# Acceptance Rate : 87.8%
# Likes           : 612
# Dislikes        : 77
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12296000  (beats 91.6505%)
# Submitted  : 1774475558
#
# --- Hints ---
# Iterate over the elements of array hours and check if the value is greater than or equal to target.
# ================================================================

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in hours:
            if i >= target:
                count+=1
        return count
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        
