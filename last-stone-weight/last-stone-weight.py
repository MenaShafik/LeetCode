# ==========================================================
# Problem    : Last Stone Weight
# URL        : https://leetcode.com/problems/last-stone-weight/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Heap (Priority Queue)
#
# Acceptance : 66.6%
# Likes      : 6723  |  Dislikes: 156
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12344000  (beats 53.344100000000005%)
# Submitted  : 1782904418
# Exported   : 2026-07-01 11:15:42 UTC
#
# Hints: Simulate the process.  We can do it with a heap, or by sorting some list of stones every time we take a turn.
# ==========================================================
class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x != y:
                stones.append(y - x)
        return stones[0] if stones else 0
        """
        :type stones: List[int]
        :rtype: int
        """
        
