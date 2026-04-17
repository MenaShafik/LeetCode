# ================================================================
# Problem : How Many Numbers Are Smaller Than the Current Number
# URL     : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting, Counting Sort
#
# --- Community Stats ---
# Acceptance Rate : 87.4%
# Likes           : 6031
# Dislikes        : 163
#
# --- My Submission ---
# Language   : python
# Runtime    : 120  (beats 59.32599999999999%)
# Memory     : 12504000  (beats 17.401599999999988%)
# Submitted  : 1775424538
#
# --- Hints ---
# Brute force for each array element.
# In order to improve the time complexity, we can sort the array and get the answer for each array element.
# ================================================================

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in nums:
            count = 0
            for j in nums:
                if j<i:
                    count+=1
            result.append(count)
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
