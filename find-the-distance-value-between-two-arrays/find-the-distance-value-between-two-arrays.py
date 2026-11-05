# ==========================================================
# Problem    : Find the Distance Value Between Two Arrays
# URL        : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers, Binary Search, Sorting
#
# Acceptance : 78.2%
# Likes      : 1277  |  Dislikes: 3336
#
# Language   : python
# Runtime    : 18  (beats 68.58239999999998%)
# Memory     : 12280000  (beats 81.60919999999999%)
# Submitted  : 1793868028
# Exported   : 2026-11-05 21:43:31 UTC
#
# Hints: Sort 'arr2' and use binary search to get the closest element for each 'arr1[i]', it gives a time complexity of O(nlogn).
# ==========================================================
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        counter =  0
        for i  in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    break
            else:
                counter +=1
        return counter
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        
