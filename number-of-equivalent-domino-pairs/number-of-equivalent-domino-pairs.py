# ==========================================================
# Problem    : Number of Equivalent Domino Pairs
# URL        : https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 60.8%
# Likes      : 1128  |  Dislikes: 379
#
# Language   : python
# Runtime    : 5  (beats 93.9655%)
# Memory     : 19032000  (beats 16.3793%)
# Submitted  : 1787943018
# Exported   : 2026-08-28 19:31:41 UTC
#
# Hints: For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.
#   You can keep track of what you've seen using a hashmap.
# ==========================================================
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count=[0]*100
        res=0
        for a,b in dominoes:
            if a<b:
                val=a*10+b
            else:
                val=b*10+a
            res+=count[val]
            count[val]+=1
        return res
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        
