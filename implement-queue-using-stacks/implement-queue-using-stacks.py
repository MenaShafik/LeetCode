# ==========================================================
# Problem    : Implement Queue using Stacks
# URL        : https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Stack, Design, Queue
#
# Acceptance : 70.2%
# Likes      : 8753  |  Dislikes: 497
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12368000  (beats 64.7693%)
# Submitted  : 1786870633
# Exported   : 2026-08-16 22:18:02 UTC
#
# Hints: N/A
# ==========================================================
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
