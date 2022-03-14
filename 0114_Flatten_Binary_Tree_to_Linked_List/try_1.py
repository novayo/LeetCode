# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def recr(node):
            if not node:
                return
            
            left = recr(node.left)
            right = recr(node.right)
            
            node.left = None
            
            if left:
                tmp = left
                while tmp and tmp.right:
                    tmp = tmp.right
                tmp.right = right
                node.right = left
            else:
                node.right = right
            
            return node
        
        recr(root)