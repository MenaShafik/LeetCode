# ==========================================================
# Problem    : Exclusive Time of Functions
# URL        : https://leetcode.com/problems/exclusive-time-of-functions/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Stack
#
# Acceptance : 66.2%
# Likes      : 2375  |  Dislikes: 2995
#
# Language   : python
# Runtime    : 13  (beats 94.53370000000002%)
# Memory     : 12324000  (beats 79.0997%)
# Submitted  : 1779958011
# Exported   : 2026-05-28 09:03:37 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        exclusive_time = [0] * n
        prev_time = 0

        for log in logs:
            function_id, typ, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)

            if typ == 'start':
                if stack:
                    exclusive_time[stack[-1]] += timestamp - prev_time

                stack.append(function_id)
                prev_time = timestamp

            else:  # end
                exclusive_time[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return exclusive_time
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
