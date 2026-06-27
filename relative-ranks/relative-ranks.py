# ==========================================================
# Problem    : Relative Ranks
# URL        : https://leetcode.com/problems/relative-ranks/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sorting, Heap (Priority Queue)
#
# Acceptance : 74.8%
# Likes      : 2198  |  Dislikes: 152
#
# Language   : python
# Runtime    : 2  (beats 96.7651%)
# Memory     : 13324000  (beats 29.395200000000003%)
# Submitted  : 1782555948
# Exported   : 2026-06-27 10:28:19 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def findRelativeRanks(self, score):
        sorted_scores = sorted(score, reverse=True)
        map_ = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                map_[s] = "Gold Medal"
            elif i == 1:
                map_[s] = "Silver Medal"
            elif i == 2:
                map_[s] = "Bronze Medal"
            else:
                map_[s] = str(i + 1)

        return [map_[s] for s in score]

        """
        :type score: List[int]
        :rtype: List[str]
        """
        
