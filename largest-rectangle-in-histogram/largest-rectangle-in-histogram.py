# ==========================================================
# Problem    : Largest Rectangle in Histogram
# URL        : https://leetcode.com/problems/largest-rectangle-in-histogram/
# Difficulty : Hard
# Category   : Algorithms
# Tags       : Array, Stack, Monotonic Stack
#
# Acceptance : 49.9%
# Likes      : 19736  |  Dislikes: 394
#
# Language   : python
# Runtime    : 205  (beats 72.30149999999993%)
# Memory     : 20880000  (beats 83.54319999999998%)
# Submitted  : 1780130528
# Exported   : 2026-05-30 08:56:17 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_=0
        index=0

        while index < len(heights):
            if not stack or heights[index]>= heights[stack[-1]]:
                stack.append(index)
                index+=1
            else:
                top = stack.pop()
                area = (heights[top] *
                        ((index - stack[-1] - 1) if stack else index))
                max_ = max(max_, area)
        while stack:
            top = stack.pop()
            area = (heights[top] *  ((index - stack[-1] - 1) if stack else index))
            max_ = max(max_, area)
        return max_

        """
        :type heights: List[int]
        :rtype: int
        """
        
