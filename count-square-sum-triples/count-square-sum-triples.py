# ==========================================================
# Problem    : Count Square Sum Triples
# URL        : https://leetcode.com/problems/count-square-sum-triples/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Enumeration
#
# Acceptance : 77.1%
# Likes      : 744  |  Dislikes: 65
#
# Language   : python
# Runtime    : 193  (beats 75.51040000000008%)
# Memory     : 12340000  (beats 54.081600000000016%)
# Submitted  : 1777577138
# Exported   : 2026-04-30 19:44:33 UTC
#
# Hints: Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n
#   You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt
# ==========================================================
class Solution(object):
    def countTriples(self, n):
        count = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                k_sq = i*i + j*j
                k = int(k_sq ** 0.5)
                if k <= n and k * k == k_sq:
                    count += 1 if i == j else 2
        return count

        """
        :type n: int
        :rtype: int
        """
        
