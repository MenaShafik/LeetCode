# ==========================================================
# Problem    : Element Appearing More Than 25% In Sorted Array
# URL        : https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 61.5%
# Likes      : 1796  |  Dislikes: 85
#
# Language   : python
# Runtime    : 3  (beats 62.65050000000001%)
# Memory     : 13120000  (beats 76.70679999999999%)
# Submitted  : 1793171962
# Exported   : 2026-10-29 08:11:31 UTC
#
# Hints: Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%]
#   The answer should be in one of the ends of the intervals.
#   In order to check which is element is the answer we can count the frequency with binarySearch.
# ==========================================================
class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        freq = {}
        for i in arr:
            freq[i]=freq.get(i,0)+1
            if freq[i] > 0.25 * n:
                return i

        """
        :type arr: List[int]
        :rtype: int
        """
        
