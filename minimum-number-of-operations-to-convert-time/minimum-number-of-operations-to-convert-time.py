# ==========================================================
# Problem    : Minimum Number of Operations to Convert Time
# URL        : https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : String, Greedy
#
# Acceptance : 66.5%
# Likes      : 506  |  Dislikes: 39
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12448000  (beats 18.0%)
# Submitted  : 1788638976
# Exported   : 2026-09-05 20:25:13 UTC
#
# Hints: Convert the times to minutes.
#   Use the operation with the biggest value possible at each step.
# ==========================================================
class Solution(object):
    def convertTime(self, current, correct):
        current = current.split(":")
        correct = correct.split(":")

        current_mins = int(current[0]) * 60 + int(current[1])
        correct_mins = int(correct[0]) * 60 + int(correct[1])

        difference = correct_mins - current_mins
        counter = 0

        counter += difference // 60
        difference %= 60

        counter += difference // 15
        difference %= 15

        counter += difference // 5
        difference %= 5

        counter += difference

        return counter
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        
