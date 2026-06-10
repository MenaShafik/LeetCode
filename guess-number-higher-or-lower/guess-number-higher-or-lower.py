# ==========================================================
# Problem    : Guess Number Higher or Lower
# URL        : https://leetcode.com/problems/guess-number-higher-or-lower/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Binary Search, Interactive
#
# Acceptance : 57.6%
# Likes      : 4281  |  Dislikes: 699
#
# Language   : python
# Runtime    : 7  (beats 97.1663%)
# Memory     : 12368000  (beats 53.616699999999994%)
# Submitted  : 1781122058
# Exported   : 2026-06-10 20:13:07 UTC
#
# Hints: N/A
# ==========================================================
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1
        """
        :type n: int
        :rtype: int
        """
        
