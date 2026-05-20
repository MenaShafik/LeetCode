# ==========================================================
# Problem    : Remove Duplicates from Sorted Array
# URL        : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Two Pointers
#
# Acceptance : 62.8%
# Likes      : 19245  |  Dislikes: 20546
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13868000  (beats 42.9405%)
# Submitted  : 1779262739
# Exported   : 2026-05-20 07:40:21 UTC
#
# Hints: In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned, what is their positioning in the array when the given array is sorted? Look at the image below for the answer. If we know the position of one of the elements, do we also know the positioning of all the duplicate elements?

<br>
<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_rem_dup.png" width="500"/>
#   We need to modify the array in-place and the size of the final array would potentially be smaller than the size of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.
#   Essentially, once an element is encountered, you simply need to <b>bypass</b> its duplicates and move on to the next unique element.
# ==========================================================
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        write_index = 1
        
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
        """
        :type nums: List[int]
        :rtype: int
        """
        
