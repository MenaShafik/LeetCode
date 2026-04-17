# ================================================================
# Problem : Average Salary Excluding the Minimum and Maximum Salary
# URL     : https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 63.5%
# Likes           : 2280
# Dislikes        : 187
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12356000  (beats 57.692299999999996%)
# Submitted  : 1774646897
#
# --- Hints ---
# Get the total sum and subtract the minimum and maximum value in the array.  Finally divide the result by n - 2.
# ================================================================

class Solution(object):
    def average(self, salary):
        total = sum(salary) 
        return (total - min(salary) - max(salary)) / float(len(salary) - 2)
        """
        :type salary: List[int]
        :rtype: float
        """
        
