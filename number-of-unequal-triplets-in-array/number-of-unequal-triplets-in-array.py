# ==========================================================
# Problem    : Number of Unequal Triplets in Array
# URL        : https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 73.6%
# Likes      : 465  |  Dislikes: 50
#
# Language   : python
# Runtime    : 290  (beats 82.2222%)
# Memory     : 12396000  (beats 55.555600000000005%)
# Submitted  : 1789633995
# Exported   : 2026-09-18 21:35:06 UTC
#
# Hints: The constraints are very small. Can we try every triplet?
#   Yes, we can. Use three loops to iterate through all the possible triplets, ensuring the condition i < j < k holds.
# ==========================================================
class Solution(object):
    def unequalTriplets(self, nums):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    continue
                for k in range(j+1,len(nums)):
                    if nums[j] != nums[k] and nums[i] != nums[k]:
                        counter+=1
        return counter
        """
        :type nums: List[int]
        :rtype: int
        """
        
