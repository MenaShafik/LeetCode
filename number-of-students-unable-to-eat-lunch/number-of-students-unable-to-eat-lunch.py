# ==========================================================
# Problem    : Number of Students Unable to Eat Lunch
# URL        : https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Stack, Queue, Simulation
#
# Acceptance : 80.0%
# Likes      : 2799  |  Dislikes: 302
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12368000  (beats 59.649100000000004%)
# Submitted  : 1790361268
# Exported   : 2026-09-26 08:43:44 UTC
#
# Hints: Simulate the given in the statement
#   Calculate those who will eat instead of those who will not.
# ==========================================================
class Solution(object):
    def countStudents(self, students, sandwiches):
        zeros = students.count(0)
        ones = students.count(1)

        for sandwich in sandwiches:
            if sandwich == 0:
                if zeros == 0:
                    return ones
                zeros -= 1
            else:
                if ones == 0:
                    return zeros
                ones -= 1

        return 0
  
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        
