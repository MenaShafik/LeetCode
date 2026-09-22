# ==========================================================
# Problem    : Largest Number
# URL        : https://leetcode.com/problems/largest-number/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, String, Greedy, Sorting
#
# Acceptance : 43.8%
# Likes      : 9598  |  Dislikes: 812
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12480000  (beats 70.90559999999999%)
# Submitted  : 1790066228
# Exported   : 2026-09-22 10:13:20 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def largestNumber(self, nums):
        s=list(map(str,nums))
        s.sort(key=lambda x: x*10,reverse=True)
        if s[0]=="0":
            return "0"
        return "".join(s) 
                
        """
        :type nums: List[int]
        :rtype: str
        """
        
