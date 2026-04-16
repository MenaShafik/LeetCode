# ================================================================
# Problem : Contains Duplicate
# URL     : https://leetcode.com/problems/contains-duplicate/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 64.2%
# Likes           : 13964
# Dislikes        : 1372
#
# --- My Submission ---
# Language   : python
# Runtime    : 15  (beats 76.29529999999998%)
# Memory     : 25816000  (beats 61.716400000000064%)
# Submitted  : 1773438038
#
# --- Hints ---
# N/A
# ================================================================

class Solution(object):
    def containsDuplicate(self, nums):
            seen = set()
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False
