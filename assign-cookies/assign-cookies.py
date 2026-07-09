# ==========================================================
# Problem    : Assign Cookies
# URL        : https://leetcode.com/problems/assign-cookies/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Greedy, Sorting
#
# Acceptance : 55.2%
# Likes      : 5100  |  Dislikes: 460
#
# Language   : python
# Runtime    : 17  (beats 99.08189999999999%)
# Memory     : 14000000  (beats 87.47919999999998%)
# Submitted  : 1783609229
# Exported   : 2026-07-09 15:04:13 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort(reverse = True)
        s.sort(reverse = True)
        j = 0
        res = 0
        for c in g:
            if j >= len(s):
                break
            if s[j] >= c:
                res += 1
                j += 1
        return res
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
