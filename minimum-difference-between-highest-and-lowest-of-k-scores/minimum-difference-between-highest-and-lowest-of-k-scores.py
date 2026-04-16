# ================================================================
# Problem : Minimum Difference Between Highest and Lowest of K Scores
# URL     : https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Sliding Window, Sorting
#
# --- Community Stats ---
# Acceptance Rate : 66.2%
# Likes           : 1462
# Dislikes        : 376
#
# --- My Submission ---
# Language   : python
# Runtime    : 10  (beats 64.80830000000002%)
# Memory     : 12616000  (beats 12.19509999999999%)
# Submitted  : 1769350919
#
# --- Hints ---
# For the difference between the highest and lowest element to be minimized, the k chosen scores need to be as close to each other as possible.
# What if the array was sorted?
# After sorting the scores, any contiguous k scores are as close to each other as possible.
# Apply a sliding window solution to iterate over each contiguous k scores, and find the minimum of the differences of all windows.
# ================================================================

class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0
                
        nums.sort()
                
        l = 0
        r = k - 1
        mn = float('inf')
                
        while r < len(nums):
            mn = min(mn, nums[r] - nums[l])
            l += 1
            r += 1
                
        return mn
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
