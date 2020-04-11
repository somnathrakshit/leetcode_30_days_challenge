# Title: Diameter of Binary Tree
# URL: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        
        def find_depth(n):
            if not n:
                return 0
            left = find_depth(n.left)
            right = find_depth(n.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
        
        find_depth(root)
        return self.ans
