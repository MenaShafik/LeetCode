# ==========================================================
# Problem    : Find Maximum Number of String Pairs
# URL        : https://leetcode.com/problems/find-maximum-number-of-string-pairs/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, String, Simulation
#
# Acceptance : 82.5%
# Likes      : 491  |  Dislikes: 19
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12320000  (beats 55.555600000000005%)
# Submitted  : 1790670585
# Exported   : 2026-09-29 09:52:18 UTC
#
# Hints: Notice that array words consist of distinct strings.
#   Iterate over all indices (i, j) and check if they can be paired.
# ==========================================================
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        counter = 0
        map_ = {}
        for i in words:
            if i[::-1] in map_:
                counter+=1
            else:
                map_[i] =1
        return counter
        """
        :type words: List[str]
        :rtype: int
        """
        
