# ==========================================================
# Problem    : Unique Number of Occurrences
# URL        : https://leetcode.com/problems/unique-number-of-occurrences/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 78.8%
# Likes      : 5621  |  Dislikes: 156
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12488000  (beats 54.0047%)
# Submitted  : 1785496393
# Exported   : 2026-07-31 11:32:50 UTC
#
# Hints: Find the number of occurrences of each element in the array using a hash map.
#   Iterate through the hash map and check if there is a repeated value.
# ==========================================================
class Solution(object):
    def uniqueOccurrences(self, arr):
        mapp = {}
        for i in arr:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1
        counts = list(mapp.values())
        return len(counts) == len(set(counts))           
        """
        :type arr: List[int]
        :rtype: bool
        """
        
