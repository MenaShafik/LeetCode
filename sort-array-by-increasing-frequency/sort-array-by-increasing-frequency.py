# ==========================================================
# Problem    : Sort Array by Increasing Frequency
# URL        : https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table, Sorting
#
# Acceptance : 81.1%
# Likes      : 3800  |  Dislikes: 187
#
# Language   : python
# Runtime    : 2  (beats 80.2395%)
# Memory     : 12056000  (beats 98.004%)
# Submitted  : 1792655301
# Exported   : 2026-10-22 10:56:57 UTC
#
# Hints: Count the frequency of each value.
#   Use a custom comparator to compare values by their frequency. If two values have the same frequency, compare their values.
# ==========================================================
class Solution(object):
    def frequencySort(self, nums):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
