# ==========================================================
# Problem    : Partition Array Into Three Parts With Equal Sum
# URL        : https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Greedy
#
# Acceptance : 42.9%
# Likes      : 1819  |  Dislikes: 169
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 16308000  (beats 5.555600000000007%)
# Submitted  : 1785403008
# Exported   : 2026-07-30 10:43:34 UTC
#
# Hints: If we have three parts with the same sum, what is the sum of each?
If you can find the first part, can you find the second part?
# ==========================================================
class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 !=0:
            return False
        target = total // 3
        run =0
        parts = 0
        for i in range(len(arr)-1):
            run+= arr[i]
            if run == target:
                parts+=1
                run =0
                if parts ==2:
                    return True
        return False
        """
        :type arr: List[int]
        :rtype: bool
        """
        
