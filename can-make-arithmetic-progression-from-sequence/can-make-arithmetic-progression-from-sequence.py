# ==========================================================
# Problem    : Can Make Arithmetic Progression From Sequence
# URL        : https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting
#
# Acceptance : 68.9%
# Likes      : 2347  |  Dislikes: 120
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12276000  (beats 99.0717%)
# Submitted  : 1779529782
# Exported   : 2026-05-23 09:51:39 UTC
#
# Hints: Consider that any valid arithmetic progression will be in sorted order.
#   Sort the array, then check if the differences of all consecutive elements are equal.
# ==========================================================
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
        
        """
        :type arr: List[int]
        :rtype: bool
        """
        
