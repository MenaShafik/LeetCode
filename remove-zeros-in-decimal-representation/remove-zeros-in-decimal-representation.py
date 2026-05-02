# ==========================================================
# Problem    : Remove Zeros in Decimal Representation
# URL        : https://leetcode.com/problems/remove-zeros-in-decimal-representation/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math, Simulation
#
# Acceptance : 76.4%
# Likes      : 46  |  Dislikes: 2
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12488000  (beats 13.709700000000005%)
# Submitted  : 1777754991
# Exported   : 2026-05-02 21:10:16 UTC
#
# Hints: Convert to a string and filter out the <code>'0'</code> characters.
# ==========================================================
class Solution(object):
    def removeZeros(self, n):
        result = []
        for i in str(n):
            if i != "0":
                result.append(i)
        return int(''.join(result))

        """
        :type n: int
        :rtype: int
        """
        
