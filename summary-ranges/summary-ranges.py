# ==========================================================
# Problem    : Summary Ranges
# URL        : https://leetcode.com/problems/summary-ranges/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 54.2%
# Likes      : 4548  |  Dislikes: 2388
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12348000  (beats 55.916999999999994%)
# Submitted  : 1777671250
# Exported   : 2026-05-01 21:39:06 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append("{}->{}".format(start, nums[i-1]))
                start = nums[i]

        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, nums[-1]))
        
        return ranges
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
