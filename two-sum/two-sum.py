# ================================================================
# Problem : Two Sum
# URL     : https://leetcode.com/problems/two-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# --- Community Stats ---
# Acceptance Rate : 57.4%
# Likes           : 68670
# Dislikes        : 2569
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13044000  (beats 71.6186%)
# Submitted  : 1768684561
#
# --- Hints ---
# A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.
# So, if we fix one of the numbers, say <code>x</code>, we have to scan the entire array to find the next number <code>y</code> which is <code>value - x</code> where value is the input parameter. Can we change our array somehow so that this search becomes faster?
# The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
# ================================================================

class Solution(object):
    def twoSum(self, nums, target):

            self.nums = nums
            self.target = target
            seen = {}
            for i,num in enumerate(nums):
                needed = target - num
                if needed in seen:
                 return   seen[needed],i
                else:
                    seen[num] = i
