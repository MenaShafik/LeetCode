# ==========================================================
# Problem    : Remove Element
# URL        : https://leetcode.com/problems/remove-element/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers
#
# Acceptance : 62.8%
# Likes      : 5617  |  Dislikes: 5498
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 11872000  (beats 98.8794%)
# Submitted  : 1795594565
# Exported   : 2026-11-25 08:26:20 UTC
#
# Hints: The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to <b>remove</b> that element per se, right?
#   We can move all the occurrences of this element to the end of the array. Use two pointers!
<br><img src="https://assets.leetcode.com/uploads/2019/10/20/hint_remove_element.png" width="500"/>
#   Yet another direction of thought is to consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.
# ==========================================================
class Solution(object):
    def removeElement(self, nums, val):
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter +=1
        return counter
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
