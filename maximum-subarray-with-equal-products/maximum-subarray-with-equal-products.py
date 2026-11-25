# ==========================================================
# Problem    : Maximum Subarray With Equal Products
# URL        : https://leetcode.com/problems/maximum-subarray-with-equal-products/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Math, Sliding Window, Enumeration, Number Theory
#
# Acceptance : 60.4%
# Likes      : 296  |  Dislikes: 90
#
# Language   : python
# Runtime    : 91  (beats 61.11080000000001%)
# Memory     : 12240000  (beats 27.7778%)
# Submitted  : 1795509388
# Exported   : 2026-11-25 08:26:22 UTC
#
# Hints: What is the maximum possible lcm?
# ==========================================================
class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)
        counter = 0
        for i in range(len(nums)):
            p = 1
            g = nums[i]
            l = nums[i]
            for j in range(i,len(nums)):
                p*=nums[j]
                g = gcd(g,nums[j])
                l = lcm(l,nums[j])
                if p == g * l:
                    counter =  max(counter,j-i+1)
        return counter

        """
        :type nums: List[int]
        :rtype: int
        """
        
