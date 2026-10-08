# ==========================================================
# Problem    : Number of Intersecting Interval Pairs I
# URL        : https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Binary Search, Sorting, Enumeration
#
# Acceptance : 61.7%
# Likes      : 26  |  Dislikes: 0
#
# Language   : python
# Runtime    : 79  (beats 69.04470000000008%)
# Memory     : 12472000  (beats 31.981399999999994%)
# Submitted  : 1791444008
# Exported   : 2026-10-08 13:40:11 UTC
#
# Hints: <p>Check every pair of intervals. They intersect exactly when <code>max(start<sub>i</sub>, start<sub>j</sub>) &lt;= min(end<sub>i</sub>, end<sub>j</sub>)</code>.</p>
# ==========================================================
class Solution(object):
    def countIntersectingIntervals(self, intervals):
        counter = 0
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                    counter+=1
        return counter
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
