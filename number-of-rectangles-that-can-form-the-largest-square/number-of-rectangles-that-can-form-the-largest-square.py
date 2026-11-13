# ==========================================================
# Problem    : Number Of Rectangles That Can Form The Largest Square
# URL        : https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array
#
# Acceptance : 79.6%
# Likes      : 631  |  Dislikes: 76
#
# Language   : python
# Runtime    : 142  (beats 62.222599999999986%)
# Memory     : 12764000  (beats 60.0%)
# Submitted  : 1794608328
# Exported   : 2026-11-13 22:25:30 UTC
#
# Hints: What is the length of the largest square the can be cut out of some rectangle? It'll be equal to min(rectangle.length, rectangle.width). Replace each rectangle with this value.
#   Calculate maxSize by iterating over the given rectangles and maximizing the answer with their values denoted in the first hint.
#   Then iterate again on the rectangles and calculate the number whose values = maxSize.
# ==========================================================
class Solution(object):
    def countGoodRectangles(self, rectangles):
        stack = []
        for i in rectangles:
            mini = min(i)
            stack.append(mini)
        largest = max(stack)
        
        return stack.count(largest)
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
