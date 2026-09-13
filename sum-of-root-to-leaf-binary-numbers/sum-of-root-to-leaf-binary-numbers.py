# ==========================================================
# Problem    : Sum of Root To Leaf Binary Numbers
# URL        : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Tree, Depth-First Search, Binary Tree
#
# Acceptance : 76.7%
# Likes      : 3816  |  Dislikes: 212
#
# Language   : python
# Runtime    : 0  (beats 100.0%)
# Memory     : 12992000  (beats 54.983999999999995%)
# Submitted  : 1789288275
# Exported   : 2026-09-13 10:48:08 UTC
#
# Hints: Find each path, then transform that path to an integer in base 10.
# ==========================================================
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):

        def dfs(node, number):

            if node is None:
                return 0

            number = number * 2 + node.val

            if node.left is None and node.right is None:
                return number

            left = dfs(node.left, number)
            right = dfs(node.right, number)

            return left + right

        return dfs(root, 0)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
