# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        def dfs(node):
            nonlocal ans
            
            if ans != None:
                return 0
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            ret = left + right
            if node.val in [p.val, q.val]:
                ret += 1
            
            if not ans and ret == 2:
                ans = node
            
            return ret
            
        dfs(root)
        return ans
