# ==========================================================
# Problem    : Evaluate Reverse Polish Notation
# URL        : https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Array, Math, Stack
#
# Acceptance : 57.8%
# Likes      : 8764  |  Dislikes: 1195
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 13512000  (beats 80.7465%)
# Submitted  : 1779872557
# Exported   : 2026-05-27 09:07:27 UTC
#
# Hints: N/A
# ==========================================================
class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y)
        }

        for i in tokens:
            if i in operations:
                pop_b = stack.pop()
                pop_a = stack.pop()

                result = operations[i](pop_a, pop_b)
                stack.append(result)
            else:
                stack.append(int(i))

        return stack[0]
        """
        :type tokens: List[str]
        :rtype: int
        """
        
