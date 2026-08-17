# ==========================================================
# Problem    : Add Two Numbers
# URL        : https://leetcode.com/problems/add-two-numbers/
# Difficulty : Medium
# Category   : Algorithms
# Tags       : Linked List, Math, Recursion
#
# Acceptance : 49.1%
# Likes      : 37209  |  Dislikes: 7286
#
# Language   : python
# Runtime    : 5  (beats 72.28779999999999%)
# Memory     : 12488000  (beats 58.08709999999998%)
# Submitted  : 1786957448
# Exported   : 2026-08-17 21:47:23 UTC
#
# Hints: N/A
# ==========================================================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result1 = 0
        result2 = 0

        power = 0
        while l1:
            result1 += l1.val * (10 ** power)
            power += 1
            l1 = l1.next

        power = 0
        while l2:
            result2 += l2.val * (10 ** power)
            power += 1
            l2 = l2.next

        result = result1 + result2

        result = str(result)[::-1]

        head = ListNode(int(result[0]))
        current = head

        for i in range(1, len(result)):
            current.next = ListNode(int(result[i]))
            current = current.next

        return head
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
