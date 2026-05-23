# ==========================================================
# Problem    : Set Mismatch
# URL        : https://leetcode.com/problems/set-mismatch/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Bit Manipulation, Sorting
#
# Acceptance : 43.6%
# Likes      : 5509  |  Dislikes: 1413
#
# Language   : python
# Runtime    : 5  (beats 90.0275%)
# Memory     : 13948000  (beats 38.94779999999997%)
# Submitted  : 1779467361
# Exported   : 2026-05-23 09:51:43 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
