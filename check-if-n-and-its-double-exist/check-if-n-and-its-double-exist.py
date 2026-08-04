# ==========================================================
# Problem    : Check If N and Its Double Exist
# URL        : https://leetcode.com/problems/check-if-n-and-its-double-exist/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Two Pointers, Binary Search, Sorting
#
# Acceptance : 41.9%
# Likes      : 2546  |  Dislikes: 259
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12356000  (beats 78.7037%)
# Submitted  : 1785833495
# Exported   : 2026-08-04 22:21:34 UTC
#
# Hints: Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
#   On each step of the loop check if we have seen the element <code>2 * arr[i]</code> so far.
#   Also check if we have seen <code>arr[i] / 2</code> in case <code>arr[i] % 2 == 0</code>.
# ==========================================================
class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for i in arr:
            if i*2 in seen:
                return True
            if i % 2 == 0 and i // 2 in seen:
                return True
            seen.add(i)
            
        return False
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if i != j and arr[i] == 2 * arr[j]:
        #             return True
        # return False
        """
        :type arr: List[int]
        :rtype: bool
        """
        
