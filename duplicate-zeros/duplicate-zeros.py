# ==========================================================
# Problem    : Duplicate Zeros
# URL        : https://leetcode.com/problems/duplicate-zeros/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers
#
# Acceptance : 53.7%
# Likes      : 2866  |  Dislikes: 799
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12588000  (beats 84.09960000000001%)
# Submitted  : 1782638138
# Exported   : 2026-06-28 09:27:11 UTC
#
# Hints: This is a great introductory problem for understanding and working with the concept of in-place operations. The problem statement clearly states that we are to modify the array in-place. That does not mean we cannot use another array. We just don't have to return anything.
#   A better way to solve this would be without using additional space. The only reason the problem statement allows you to make modifications in place is that it hints at avoiding any additional memory.
#   The main problem with not using additional memory is that we might override elements due to the zero duplication requirement of the problem statement. How do we get around that?
#   If we had enough space available, we would be able to accommodate all the elements properly. The new length would be the original length of the array plus the number of zeros. Can we use this information somehow to solve the problem?
# ==========================================================
class Solution(object):
    def duplicateZeros(self, arr):
        temp = []

        for num in arr:
            temp.append(num)
            if num == 0:
                temp.append(0)

        for i in range(len(arr)):
            arr[i] = temp[i]
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
