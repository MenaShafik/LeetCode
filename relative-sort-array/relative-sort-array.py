# ==========================================================
# Problem    : Relative Sort Array
# URL        : https://leetcode.com/problems/relative-sort-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting, Counting Sort
#
# Acceptance : 75.3%
# Likes      : 3385  |  Dislikes: 201
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12524000  (beats 20.210500000000003%)
# Submitted  : 1783093319
# Exported   : 2026-07-03 15:52:00 UTC
#
# Hints: Using a hashmap, we can map the values of arr2 to their position in arr2.
#   After, we can use a custom sorting function.
# ==========================================================
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        
        remaining = sorted(count.keys())
        for num in remaining:
            result.extend([num] * count[num])
        
        return result
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
