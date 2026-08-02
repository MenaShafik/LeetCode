# ==========================================================
# Problem    : Kth Missing Positive Number
# URL        : https://leetcode.com/problems/kth-missing-positive-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Binary Search
#
# Acceptance : 63.8%
# Likes      : 8130  |  Dislikes: 583
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12548000  (beats 17.46719999999999%)
# Submitted  : 1785578624
# Exported   : 2026-08-02 16:15:43 UTC
#
# Hints: Keep track of how many positive numbers are missing as you scan the array.
# ==========================================================
class Solution(object):
    def findKthPositive(self, arr, k):
        s = set(arr)
        num = 1
        count = 0

        while True:
            if num not in s:
                count += 1
                if count == k:
                    return num
            num += 1

        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
