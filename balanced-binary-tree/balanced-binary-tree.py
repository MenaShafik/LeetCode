# ================================================================
# Problem : Balanced Binary Tree
# URL     : https://leetcode.com/problems/balanced-binary-tree/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Tree, Depth-First Search, Binary Tree
#
# --- Community Stats ---
# Acceptance Rate : 58.2%
# Likes           : 12213
# Dislikes        : 842
#
# --- My Submission ---
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 17312000  (beats 85.4512%)
# Submitted  : 1770576629
#
# --- Hints ---
# N/A
# ================================================================

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        return self.checkHeight(root) != -1

    def checkHeight(self, node):
        if node is None:
            return 0

        left_height = self.checkHeight(node.left)
        if left_height == -1:
            return -1

        right_height = self.checkHeight(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1 
        return max(left_height, right_height) + 1
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
