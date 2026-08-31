# ==========================================================
# Problem    : Unique 3-Digit Even Numbers
# URL        : https://leetcode.com/problems/unique-3-digit-even-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Recursion, Enumeration
#
# Acceptance : 70.5%
# Likes      : 141  |  Dislikes: 35
#
# Language   : python
# Runtime    : 12  (beats 94.5313%)
# Memory     : 12304000  (beats 64.0626%)
# Submitted  : 1788165755
# Exported   : 2026-08-31 08:59:03 UTC
#
# Hints: Use brute force to try all possibilities
# ==========================================================
from itertools import permutations


class Solution(object):
    def totalNumbers(self, digits):
        results = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            if perm[2] % 2 != 0:
                continue
            results.add(perm[0] * 100 + perm[1] * 10 + perm[2])
        return len(results)
        """
        :type digits: List[int]
        :rtype: int
        """
        
