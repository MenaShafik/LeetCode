# ==========================================================
# Problem    : Divisible and Non-divisible Sums Difference
# URL        : https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Math
#
# Acceptance : 91.0%
# Likes      : 677  |  Dislikes: 37
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12552000  (beats 0.8389000000000095%)
# Submitted  : 1778495668
# Exported   : 2026-05-11 10:35:37 UTC
#
# Hints: With arithmetic progression we know that the sum of integers in the range <code>[1, n]</code> is <code>n * (n + 1) / 2 </code>.
# ==========================================================
class Solution(object):
    def differenceOfSums(self, n, m):
        nums = []
        mums=[]
        for i in range(1, n + 1):
            if i % m != 0:
                nums.append(i)
            else:
                mums.append(i)
        return (sum(nums) - sum(mums))
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
