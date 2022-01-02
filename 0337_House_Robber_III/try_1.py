# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            
            if not node.left and not node.right:
                return node.val, 0
            
            
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            
            return l_not_rob + r_not_rob + node.val, \
                   max(l_rob + r_not_rob,
                       r_rob + l_not_rob,
                       l_rob + r_rob,
                       l_not_rob + r_not_rob
                   )
            
        return max(dfs(root))
