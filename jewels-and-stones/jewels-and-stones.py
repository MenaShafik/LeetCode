# ==========================================================
# Problem    : Jewels and Stones
# URL        : https://leetcode.com/problems/jewels-and-stones/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Hash Table, String
#
# Acceptance : 89.6%
# Likes      : 5502  |  Dislikes: 633
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12444000  (beats 16.803700000000006%)
# Submitted  : 1784108768
# Exported   : 2026-07-15 10:09:27 UTC
#
# Hints: For each stone, check if it is a jewel.
# ==========================================================
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for i in stones:
            if i in jewels:
                count+=1
        return count
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
