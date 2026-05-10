# ==========================================================
# Problem    : Mirror Distance of an Integer
# URL        : https://leetcode.com/problems/mirror-distance-of-an-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 91.5%
# Likes      : 237  |  Dislikes: 10
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12280000  (beats 88.5869%)
# Submitted  : 1778403582
# Exported   : 2026-05-10 09:01:20 UTC
#
# Hints: Simulate as described
# ==========================================================
class Solution(object):
    def mirrorDistance(self, n):
        reverse = reversed(str(n))
        return abs(n - int(''.join(reverse)))


        """
        :type n: int
        :rtype: int
        """
        
