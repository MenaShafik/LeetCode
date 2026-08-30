# ==========================================================
# Problem    : Number of Students Doing Homework at a Given Time
# URL        : https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 76.2%
# Likes      : 944  |  Dislikes: 157
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12384000  (beats 61.261300000000006%)
# Submitted  : 1787994451
# Exported   : 2026-08-30 19:04:33 UTC
#
# Hints: Imagine that startTime[i] and endTime[i] form an interval (i.e. [startTime[i], endTime[i]]).
#   The answer is how many times the queryTime laid in those mentioned intervals.
# ==========================================================
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        counter = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                counter+=1
        return counter
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        
