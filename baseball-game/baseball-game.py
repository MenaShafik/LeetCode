# ==========================================================
# Problem    : Baseball Game
# URL        : https://leetcode.com/problems/baseball-game/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Stack, Simulation
#
# Acceptance : 80.6%
# Likes      : 3391  |  Dislikes: 1971
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12520000  (beats 7.5837999999999965%)
# Submitted  : 1782472749
# Exported   : 2026-06-26 11:28:56 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def calPoints(self, operations):
        stack = []

        for i in operations:
            if i == "C":
                stack.pop()

            elif i == "D":
                stack.append(stack[-1] * 2)

            elif i == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(i))

        return sum(stack)
        """
        :type operations: List[str]
        :rtype: int
        """
        
