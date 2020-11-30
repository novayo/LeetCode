# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        def top_down(node, sumup):            
            if not node:
                return False
            
            if not node.left and not node.right:
                return sumup + node.val == sum
            
            if top_down(node.left, sumup + node.val):
                return True
            
            if top_down(node.right, sumup + node.val):
                return True
            
            return False
        
        return top_down(root, 0)
