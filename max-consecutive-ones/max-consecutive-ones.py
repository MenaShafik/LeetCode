# ==========================================================
# Problem    : Max Consecutive Ones
# URL        : https://leetcode.com/problems/max-consecutive-ones/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 65.2%
# Likes      : 6922  |  Dislikes: 500
#
# Language   : python
# Runtime    : 35  (beats 40.34700000000001%)
# Memory     : 13516000  (beats 52.91709999999999%)
# Submitted  : 1779466871
# Exported   : 2026-05-23 09:51:50 UTC
#
# Hints: You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window.

How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.
# ==========================================================
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        
        return max_count
        """
        :type nums: List[int]
        :rtype: int
        """
        
