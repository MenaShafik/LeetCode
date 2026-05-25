# ==========================================================
# Problem    : Find All Numbers Disappeared in an Array
# URL        : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 64.1%
# Likes      : 10448  |  Dislikes: 557
#
# Language   : python
# Runtime    : 23  (beats 98.3796%)
# Memory     : 26800000  (beats 75.72350000000003%)
# Submitted  : 1779708379
# Exported   : 2026-05-25 11:29:02 UTC
#
# Hints: This is a really easy problem if you decide to use additional memory. For those trying to write an initial solution using additional memory, think <b>counters!</b>
#   However, the trick really is to not use any additional space than what is already available to use. Sometimes, multiple passes over the input array help find the solution. However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.
#   The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements in the array. Can we use this information and modify the array in-place somehow to find what we need?
# ==========================================================
class Solution(object):
    def findDisappearedNumbers(self, nums):
        sets = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in sets:
                result.append(i)
        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
