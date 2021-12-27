# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        ans = None
        
        def inorder(node):
            nonlocal ans
            
            if not node:
                return
            
            if node.left and node.val > p.val:
                inorder(node.left)
            
            if node.val > p.val and (not ans or ans.val > node.val):
                ans = node
                
            if node.right and node.val <= p.val:
                inorder(node.right)
        
        inorder(root)
        return ans
