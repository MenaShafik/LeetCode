# ==========================================================
# Problem    : Find the Town Judge
# URL        : https://leetcode.com/problems/find-the-town-judge/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Graph Theory
#
# Acceptance : 50.9%
# Likes      : 6994  |  Dislikes: 634
#
# Language   : python
# Runtime    : 11  (beats 86.93680000000002%)
# Memory     : 15948000  (beats 76.57650000000001%)
# Submitted  : 1782394338
# Exported   : 2026-06-25 13:38:15 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findJudge(self, n, trust):
        if n == 1:
            return 1
        trust_count = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trust_count[a] += 1
            trusted_by[b] += 1

        for i in range(1, n + 1):
            if trust_count[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
