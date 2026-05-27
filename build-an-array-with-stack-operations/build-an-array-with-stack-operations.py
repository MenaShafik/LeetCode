# ==========================================================
# Problem    : Build an Array With Stack Operations
# URL        : https://leetcode.com/problems/build-an-array-with-stack-operations/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Stack, Simulation
#
# Acceptance : 80.9%
# Likes      : 1259  |  Dislikes: 548
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12428000  (beats 17.863100000000003%)
# Submitted  : 1779872135
# Exported   : 2026-05-27 09:07:29 UTC
#
# Hints: Use “Push” for numbers to be kept in target array and [“Push”, “Pop”] for numbers to be discarded.
# ==========================================================
class Solution(object):
    def buildArray(self, target, n):
        result = []
        j = 0

        for i in range(1, n + 1):
            if j >= len(target):
                break

            result.append("Push")

            if i == target[j]:
                j += 1
            else:
                result.append("Pop")

        return result
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
