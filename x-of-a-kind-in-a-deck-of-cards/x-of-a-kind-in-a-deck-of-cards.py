# ==========================================================
# Problem    : X of a Kind in a Deck of Cards
# URL        : https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Math, Counting, Number Theory
#
# Acceptance : 30.3%
# Likes      : 1912  |  Dislikes: 581
#
# Language   : python
# Runtime    : 5  (beats 90.24389999999998%)
# Memory     : 12456000  (beats 92.6829%)
# Submitted  : 1782207741
# Exported   : 2026-06-23 09:45:08 UTC
#
# Hints: N/A
# ==========================================================
from collections import Counter
from functools import reduce

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def hasGroupsSizeX(self, deck):
        counts = Counter(deck).values()
        return reduce(self.gcd, counts) >= 2
        """
        :type deck: List[int]
        :rtype: bool
        """
        
