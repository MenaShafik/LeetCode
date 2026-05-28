# ==========================================================
# Problem    : Daily Temperatures
# URL        : https://leetcode.com/problems/daily-temperatures/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Stack, Monotonic Stack
#
# Acceptance : 68.7%
# Likes      : 14762  |  Dislikes: 376
#
# Language   : python
# Runtime    : 159  (beats 72.00060000000005%)
# Memory     : 27052000  (beats 19.935099999999995%)
# Submitted  : 1779958918
# Exported   : 2026-05-28 09:03:33 UTC
#
# Hints: If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100.  We could remember when all of them occur next.
# ==========================================================
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
