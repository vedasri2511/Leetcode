# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        
        # If one tree is empty, return the other tree
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        # Merge current nodes
        root1.val += root2.val
        
        # Merge left and right subtrees
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1