# ==========================================================
# Problem    : Most Frequent Number Following Key In an Array
# URL        : https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Counting
#
# Acceptance : 59.7%
# Likes      : 416  |  Dislikes: 253
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12516000  (beats 45.3125%)
# Submitted  : 1789460688
# Exported   : 2026-09-15 10:59:03 UTC
#
# Hints: Count the number of times each target value follows the key in the array.
#   Choose the target with the maximum count and return it.
# ==========================================================
class Solution(object):

  def mostFrequent(self, nums, key):
    counter = {}
    max_freq = 0
    ans = 0

    for i in range(len(nums) - 1):
      if nums[i] == key:
        target = nums[i + 1]
        counter[target] = counter.get(target, 0) + 1

        if counter[target] > max_freq:
          max_freq = counter[target]
          ans = target

    return ans
        
