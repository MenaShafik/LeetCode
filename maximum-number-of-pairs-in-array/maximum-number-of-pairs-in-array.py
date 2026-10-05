# ==========================================================
# Problem    : Maximum Number of Pairs in Array
# URL        : https://leetcode.com/problems/maximum-number-of-pairs-in-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 76.3%
# Likes      : 755  |  Dislikes: 19
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12372000  (beats 57.30329999999999%)
# Submitted  : 1791186124
# Exported   : 2026-10-05 10:34:03 UTC
#
# Hints: What do we need to know to find how many pairs we can make? We need to know the frequency of each integer.
#   When will there be a leftover number? When the frequency of an integer is an odd number.
# ==========================================================
class Solution(object):
    def numberOfPairs(self, nums):
        counter = 0
        for i in set(nums):
            pairs = nums.count(i) // 2
            counter += pairs
        return [counter,len(nums) - counter * 2]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
