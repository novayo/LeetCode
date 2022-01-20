# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def recr(node):
            nonlocal ans
            if ans:
                return 0
            
            if not node:
                return 0
            
            left = recr(node.left)
            right = recr(node.right)
            
            if ans:
                return 0
            
            ret = 0
            if node == p or node == q:
                ret += 1
            
            ret += left + right
                        
            if ret == 2:
                ans = node
            
            return ret
        
        recr(root)
        return ans
