# ==========================================================
# Problem    : Convert Binary Number in a Linked List to Integer
# URL        : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Linked List, Math
#
# Acceptance : 82.4%
# Likes      : 4704  |  Dislikes: 178
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12380000  (beats 54.9668%)
# Submitted  : 1784457978
# Exported   : 2026-07-19 11:05:02 UTC
#
# Hints: Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
#   You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.
# ==========================================================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        binary = ''
        while head:
            binary += str(head.val)
            head = head.next
        result = int(binary, 2)
        return result
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
