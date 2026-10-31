# ==========================================================
# Problem    : Find Lucky Integer in an Array
# URL        : https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 75.7%
# Likes      : 1662  |  Dislikes: 46
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12352000  (beats 80.04580000000001%)
# Submitted  : 1793435029
# Exported   : 2026-10-31 11:28:21 UTC
#
# Hints: Count the frequency of each integer in the array.
#   Get all lucky numbers and return the largest of them.
# ==========================================================
class Solution(object):
    def findLucky(self, arr):
        freq = {}
        for  i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        lucky = -1
        for i in freq:
            if i == freq[i]:
                lucky = max(lucky,i)
        return lucky

        """
        :type arr: List[int]
        :rtype: int
        """
        
