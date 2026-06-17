# ==========================================================
# Problem    : Can Place Flowers
# URL        : https://leetcode.com/problems/can-place-flowers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Greedy
#
# Acceptance : 29.2%
# Likes      : 7444  |  Dislikes: 1328
#
# Language   : python
# Runtime    : 3  (beats 97.4485%)
# Memory     : 12988000  (beats 75.42530000000002%)
# Submitted  : 1781686290
# Exported   : 2026-06-17 08:53:58 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                
                flowerbed[i] = 1
                n -= 1

        return n <= 0

        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
