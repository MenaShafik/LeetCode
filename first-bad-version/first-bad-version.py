# ==========================================================
# Problem    : First Bad Version
# URL        : https://leetcode.com/problems/first-bad-version/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Binary Search, Interactive
#
# Acceptance : 47.2%
# Likes      : 9071  |  Dislikes: 3447
#
# Language   : python
# Runtime    : 10  (beats 87.61959999999998%)
# Memory     : 12312000  (beats 51.322399999999995%)
# Submitted  : 1781168649
# Exported   : 2026-06-11 10:33:10 UTC
#
# Hints: N/A
# ==========================================================
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
        """
        :type n: int
        :rtype: int
        """
        
