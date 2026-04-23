# ==========================================================
# Problem    : Earliest Time to Finish One Task
# URL        : https://leetcode.com/problems/earliest-time-to-finish-one-task/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 84.5%
# Likes      : 48  |  Dislikes: 3
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12384000  (beats 68.84060000000001%)
# Submitted  : 1776976808
# Exported   : 2026-04-23 20:41:12 UTC
#
# Hints: Compute <code>finish[i] = s[i] + t[i]</code> for each task and take the minimum.
# ==========================================================
class Solution(object):
    def earliestTime(self, tasks):
        return min(sum(task) for task in tasks)
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        
