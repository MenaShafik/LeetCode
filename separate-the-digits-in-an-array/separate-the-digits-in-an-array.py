# ==========================================================
# Problem    : Separate the Digits in an Array
# URL        : https://leetcode.com/problems/separate-the-digits-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Simulation
#
# Acceptance : 85.8%
# Likes      : 729  |  Dislikes: 18
#
# Language   : python
# Runtime    : 10  (beats 78.83760000000001%)
# Memory     : 12844000  (beats 4.769100000000009%)
# Submitted  : 1784804878
# Exported   : 2026-07-24 13:18:50 UTC
#
# Hints: Convert each number into a list and append that list to the answer.
#   You can convert the integer into a string to do that easily.
# ==========================================================
class Solution(object):
    def separateDigits(self, nums):
        stack = []
        for i in nums:
            if i >= 10:
                digits = [int(d) for d in str(i)]
                stack.extend(digits)
            else:
                stack.append(i)
        return stack

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
