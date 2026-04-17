# ================================================================
# Problem : Remove Duplicates from Sorted List
# URL     : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Linked List
#
# --- Community Stats ---
# Acceptance Rate : 56.6%
# Likes           : 9890
# Dislikes        : 377
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12396000  (beats 67.4725%)
# Submitted  : 1772281964
#
# --- Hints ---
# N/A
# ================================================================

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  
            else:
                current = current.next
        return head 
